for _ in range(int(input())):
    x1,y1 = [int(x) for x in input().split()]
    x2,y2 = [int(x) for x in input().split()]
    x3,y3 = [int(x) for x in input().split()]
    x4,y4 = [int(x) for x in input().split()]

    l = min(x1,x2,x3,x4)
    r = max(x1,x2,x3,x4)

    print(abs(l-r) * abs(l-r))