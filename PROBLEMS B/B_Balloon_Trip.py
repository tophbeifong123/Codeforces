n,q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for _ in range(q):
    lis = [int(x) for x in input().split()]
    if lis[0] == 1:
        for i in range(lis[1]-1,lis[2]):
            a[i] += lis[-1]
    else:
        ans = 0
        for i in range(lis[1]-1,lis[2]-1):
            ans += abs(a[i+1] - a[i])

        print(ans)