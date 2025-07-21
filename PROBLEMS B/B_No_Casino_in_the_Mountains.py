for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    lis = [int(x) for x in input().split()]
    count = 0
    result = 0
    for i in lis:
        if i == 0:
            count += 1
        if i == 1:
            count = 0
        if count >= k:
            result += 1
            count = -1
    print(result)