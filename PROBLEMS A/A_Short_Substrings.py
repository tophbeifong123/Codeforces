for _ in range(int(input())):
    b = list(input())
    lis = b[0]

    for i in range(len(b)):
        if i % 2 != 0:
            lis += b[i]

    print(lis)