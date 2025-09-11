for _ in range(int(input())):
    n = int(input())
    g = [int(x) for x in input().split()]
    result = 0
    g.sort(reverse=True)

    for i in range(0,n-1,2):
        result += max(g[i],g[i+1])

    if n % 2 != 0:
        result += g[-1]
    
    print(result)

