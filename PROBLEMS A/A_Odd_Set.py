for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    m,n = 0,0
    for i in a:
        if i % 2 == 0:
            m += 1
        else:
            n += 1
    if m == n:
        print("YES")
    else:
        print("NO")