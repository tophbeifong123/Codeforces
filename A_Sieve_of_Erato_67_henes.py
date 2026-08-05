for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    print('YES') if a.count(67) else print('NO')