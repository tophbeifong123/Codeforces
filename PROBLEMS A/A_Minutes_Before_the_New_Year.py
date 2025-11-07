for _ in range(int(input())):
    h,m = [int(x) for x in input().split()]
    print((23 - h)*60 + (60 - m))