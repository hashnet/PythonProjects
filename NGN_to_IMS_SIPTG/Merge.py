import sys
def mergeOnIndex(a, apKey, b, bpKey):
    print("MergeOnIndex called.")

    if len(a) < 1:
        print("A side data corrupted")
        print("exiting...")
        sys.exit(1)

    ah = a[0]
    a = a[1:]
    if apKey not in ah:
        print("Invalid key for A side. Key = ", apKey)
        print("Available Headers:")
        print(ah)
        print("exiting...")
        sys.exit(1)
    else:
        ai = ah.index(apKey)

    if len(b) < 1:
        print("B side data corrupted")
        print("exiting...")
        sys.exit(1)

    bh = b[0]
    b = b[1:]
    if bpKey not in bh:
        print("Invalid key for B side. Key = ", bpKey)
        print("Available Headers:")
        print(bh)
        print("exiting...")
        sys.exit(1)
    else:
        bi = bh.index(bpKey)

    # start processing
    # find the indices of b that doesn't have bpKey
    br = list(range(len(bh)))
    br.remove(bi)

    # prepare the header from ah and bh
    header = ah
    for i in br:
        header.append(bh[i])

    # get the search list from b
    sl = [row[bi] for row in b]

    # prepare the list from a and b
    temp = [header]
    for row in a:
        d = row
        val = row[ai]
        if val in sl:
            index = sl.index(val)
            for i in br:
                d.append(b[index][i])

        temp.append(d)

    return temp