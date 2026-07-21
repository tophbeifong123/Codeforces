for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    a = sorted([int(x) for x in input().split()])

    diff = 0
    flag = 1

    for i in range(n-1):
        if a[i+1] -  a[i] <= k:
            flag += 1
        else:
            flag = 1

        diff = max(diff,flag)
 
    if n == 1:
        print(0)
    else:
        print(n - diff)