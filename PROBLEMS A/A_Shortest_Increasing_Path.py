for _ in range(int(input())):
    x,y = [int(x) for x in input().split()]
    if x < y:
        print(2)
    elif x > y:
        if x >= y + 2 and y >= 2:
            print(3)
        else:
            print(-1)
    else:
        print(-1)