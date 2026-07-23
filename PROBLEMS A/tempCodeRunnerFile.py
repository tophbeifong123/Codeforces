for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    if len(a) % 2 == 0:
        if len(a) > 2 or (a.count(-1) == 1 and a.count(1) == 1):
            print("YES")
        else:
            print('NO')
    else:
        print("NO")