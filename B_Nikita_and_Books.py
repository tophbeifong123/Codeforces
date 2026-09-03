import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    ok = True
    prefix_sum = 0

    for i in range(n):
        prefix_sum += a[i]

        need = (i + 1) * (i + 2) // 2

        if prefix_sum < need:
            ok = False

    if ok :
        print('YES')
    else:
        print('NO')
        