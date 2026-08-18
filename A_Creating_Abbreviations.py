for _ in range(int(input())):
    n, m = map(int, input().split())

    w = set()
    ok = True

    for _ in range(n):
        w.add(input()[0].upper())

    for i in range(m):
        s = input()

        for i in s:
            if i not in w:
                ok = False
                break


    if ok:
        print('YES')
    else:
        print('NO')