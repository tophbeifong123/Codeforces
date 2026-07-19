for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    
    diff = float('inf')

    for i in range(n-1):
        if a[i+1] - a[i] < 0:
            diff = -1
            break

        diff = min(diff,a[i+1]-a[i])

    print((diff // 2) + 1)