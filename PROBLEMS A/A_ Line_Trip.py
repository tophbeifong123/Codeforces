for _ in range(int(input())):
    n,x = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    diff = a[0] 

    for i in range(n-1):
        diff = max(diff,(a[i+1] - a[i]))
    

    if (x - a[-1] ) * 2 > diff:
        print((x - a[-1] ) * 2) 
    else:
        print(diff)