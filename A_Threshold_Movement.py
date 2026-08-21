for _ in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))

    a, b = [], []

    for i in range(n):
        if i % 2 == 0:
            a.append(w[i])
        else:
            b.append(w[i])

    if n % 2 == 0 and max(b) + 1 < min(a):
        print('YES')
    else:
        print('NO')