n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = 0
for i in a:
    if i >= a[k-1] and i > 0:
        ans += 1

print(ans)