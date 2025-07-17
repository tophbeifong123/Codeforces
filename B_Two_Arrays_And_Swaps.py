for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()), reverse=True)

    for i in range(k ):
        if b[i] > a[i]:
            a[i], b[i] = b[i], a[i]


    print(a)
    print(b)
    print(sum(a))