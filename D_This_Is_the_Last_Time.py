for _ in range(int(input())):
    n, k = map(int, input().split())
    lis = []
    for _ in range(n):
        li, ri, reali = map(int, input().split())
        lis.append([li, ri, reali, True]) 
    
    changed = True
    while changed:
        changed = False
        for casino in lis:
            li, ri, reali, available = casino
            if available and li <= k <= ri and reali > k:
                k = reali
                casino[3] = False  
                changed = True
    print(k)
