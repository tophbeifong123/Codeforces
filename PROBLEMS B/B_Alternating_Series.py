for _ in range(int(input())):
    n = int(input())
    lis = []
    for i in range(1,n+1):
        if i % 2 != 0:
            lis.append(-1)
        else:
            if i == n:
                lis.append(2)
            else:
                lis.append(3)
    print(*lis)
