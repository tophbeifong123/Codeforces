for _ in range(int(input())):
    n = input()
    n = n[::-1]
    lis = []
    for i in range(len(n)-1,-1,-1):
        if int(n[i]) > 0:
            lis.append(n[i]+"0"*i)

    print(len(lis))
    print(*lis)