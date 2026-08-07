for _ in range(int(input())):
    k = int(input())
    c = [int(x) for x in input().split()]

    if max(c) > 2 or c.count(2) >= 2:
        print('YES')
    else:
        print('NO')