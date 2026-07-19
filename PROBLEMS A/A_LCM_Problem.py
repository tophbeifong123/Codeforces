for _ in range(int(input())):
    l,r = [int(x) for x in input().split()]
    
    if 2*l > r:
        print(-1,-1)
    else:
        print(l,2*l)