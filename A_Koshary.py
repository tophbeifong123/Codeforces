for _ in range(int(input())):
    x,y = [int(x) for x in input().split()]

    if x % 2 == 1 and y % 2 == 1:
        print('NO')
    else:
        print('YES')