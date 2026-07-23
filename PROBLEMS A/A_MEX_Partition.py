for _ in range(int(input())):
    n = int(input())
    a = sorted([int(x) for x in input().split()])

    ans = 0
    flag = True

    if min(a) > 0:
        print(0)
    else:
        for i in range(n-1):
            if a[i+1] - a[i] > 1:
                ans += (a[i] + 1)
                flag = False
                break
        if flag == True :
            print(max(a) + 1)
        else:
            print(ans)