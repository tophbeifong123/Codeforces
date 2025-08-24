for _ in range(int(input())):
    a,b,c = [int(x) for x in input().split()]
    if a < b and a < c and b < c:
        print("STAIR")
    elif b > a and b > c :
        print("PEAK")
    else:
        print("NONE")