for _ in range(int(input())):
    n = int(input())
    lis = []
    for i in range(len(str(n)) + 1):
        if n % (1 + 10 ** (i + 1)) == 0:
            lis.append(n //(  1 + 10 ** (i + 1)))

    if len(lis) == 0:
        print(0)
    else:    
        print(len(lis))
        print(*lis[::-1])
