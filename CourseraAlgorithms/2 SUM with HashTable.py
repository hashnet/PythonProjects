with open("files/2sum.txt", "r") as f:
# with open("files/sample2sum.txt", "r") as f:
    a = [int(line) for line in f if not line.strip() == '']
    print(a)

    d = {}
    for i in a:
        d.setdefault(i, 0)
        d[i] = d[i]+1
    print(d)

    sums = range(-10000, 10000+1)
    result = 0;
    for s in sums:
        solution = False
        st = ()

        for k in d.keys():
            if k >= s: continue

            kp = s-k
            if kp == k:
                if d[k] > 1:
                    result += 1
                    solution = True
                    st = (k, kp)
                break;

            if kp in d:
                result += 1
                solution = True
                st = (k, kp)
                break;

        print("Sum = {}, Has solution = {}, Solution = {}".format(s, solution, st))

    print("Total solutions: ", result)
