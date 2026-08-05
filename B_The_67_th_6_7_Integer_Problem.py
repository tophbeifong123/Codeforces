for _ in range(int(input())):
    a = sorted([int(x) for x in input().split()])
    print(-sum(a[0:-1])+a[-1])