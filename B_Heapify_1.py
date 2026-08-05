for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    if n % 2 == 1:
        n = n - 1

    for i in range(1, n//2 + 1):
        if a[i-1] > a[2*i-1]:
            a[i-1], a[2*i-1] = a[2*i-1], a[i-1]

    if a == sorted(a):
        print('YES')
    else:
        print('NO')