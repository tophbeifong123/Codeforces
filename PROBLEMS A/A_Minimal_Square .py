for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    print(min(max(a*2,b),max(a,b*2))**2)