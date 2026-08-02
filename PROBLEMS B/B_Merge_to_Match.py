for _ in range(int(input())):
    n,m = [int(x) for x in input().split()]
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])

    ans = 0
    left = 0
    right = 1
    
    for i in range(m):
        print(a[left],a[right])
        if a[left] + a[right] > i:
            ans += 1
            left += 2
            right += 2
        else:
            


    if ans == m:
        print('YES')
    else:
        print('NO')