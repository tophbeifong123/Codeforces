for _ in range(int(input())):
    n = int(input())
    p = [int(x) for x in input().split()]
    lis = []

    for i in range(n):
        if p[i] % 3 == 0:
            lis.append(p[i])
        else:
            d = p[i]
            while p[i] % 3 != 0:
                p[i] += 1
                if p[i] % 3 == 0:
                    lis.append(p[i] - d ) 

    print(*lis)
