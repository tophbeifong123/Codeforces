for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    m = 1
    
    for i in range(n):
        m += max(0, a[i] - b[i])

    print(m)