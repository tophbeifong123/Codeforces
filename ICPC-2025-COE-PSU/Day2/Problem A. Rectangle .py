for _ in range(int(input())):
    x1,x2,y1,y2 = [float(x) for x in input().split()]
    print(f"{abs(x1-y1) * abs(x2-y2) :.2f}")