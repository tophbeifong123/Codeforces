for _ in range(int(input())):
    n,s = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    count = abs(x[0] - s)

    if n == 1:
        print(count)
        continue
    else:
        for i in range(n-1):
            count += abs(x[i+1] - x[i])
    print(count)