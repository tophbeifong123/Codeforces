for _ in range(int(input())):
    n,m = [int(x) for x in input().split()]
    point = m
    flag = True
    for _ in range(n):
        a,b = [int(x) for x in input().split()]

        if a % 2 == 0 and flag == True:
            if b == 0:
                pass
            else:
                flag = not flag
                point -=1
        elif a % 2 == 0 and flag == False:
            if b == 0:
                flag = not flag
                point -=1
            else:
                pass
        elif a % 2 == 1 and flag == True:
            if b == 0:
                flag = not flag
                point -=1
            else:
                pass
        elif a % 2 == 1 and flag == False:
            if b == 0:
                pass
            else:
                flag = not flag
                point -=1

    print(point)

