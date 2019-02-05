def split(s, beg, end):
    lst = []

    c = s.find(beg)
    while c >= 0:
        n = s.find(end)
        if n < 0:
            break

        lst.append(s[(c + len(beg)):n].strip())
        s = s[n + len(end):]
        c = s.find(beg)

    return lst


def getval(s, title):
    s = s.strip()

    return s[len(title) + 1 :len(s) -1]


def getsubid(grp):
    for line in grp.splitlines():
        line = line.strip()

        if line.startswith('SUBID'):
            return line


def process_seg(s):
    lst = split(s, '<SUBBEGIN', '<SUBEND')
    for grp in lst:
        subid = getsubid(grp)
        subid = getval(subid, 'SUBID')

        if subid is not None:
            item = split(grp, '<IMPIBEGIN', '<IMPIEND')
            if item:
                impi = getval(item[0], 'IMPI')
            else:
                impi = ''
            item = split(grp, '<IMPUBEGIN', '<IMPUEND')
            impus = [getval(s, 'IMPU') for s in item]

            r = [subid, impi]
            for impu in impus:
                r.append(impu)

    return r, len(impus)


def process(f):
    maximpu = 0;
    t = []

    beg = '<SUBBEGIN'
    end = '<SUBEND'

    lookforbeg = True
    segment = ''
    iline = 0
    iitem = 0
    while True:
        s = f.readline()
        if s == '':
            break

        iline += 1
        if lookforbeg:
            if beg in s:
                segment = s
                lookforbeg = False
        else:
            segment += s
            if end in s:
                lookforbeg = True

                iitem += 1
                print('Processing item: {} at line {}'.format(iitem, iline), end='')
                r, cimpu = process_seg(segment)
                t.append(r)
                print(', Data: {}'.format(r))
                if cimpu > maximpu:
                    maximpu = cimpu

    t.sort(key=lambda x: x[0])

    h = ['SUBID', 'IMPI']
    for i in range(maximpu):
        h.append('IMPU'+str(i+1))

    t.insert(0, h)

    return t