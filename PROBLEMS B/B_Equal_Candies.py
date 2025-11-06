for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    total = 0
    for i in arr:
        total += i - min(arr)
    print(total)