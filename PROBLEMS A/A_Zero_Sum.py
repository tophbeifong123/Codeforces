for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    if n % 2 == 0 and sum(a) % 4 == 0:
        print('YES')
    else:
        print('NO')