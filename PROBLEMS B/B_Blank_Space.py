for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    arr = 0
    best = 0

    for i in range(n):
        if a[i] == 0:
            arr += 1
            best = max(arr,best)
        else:
            arr = 0

    print(best)