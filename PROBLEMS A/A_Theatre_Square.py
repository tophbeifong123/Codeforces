n,m,a = [int(x) for x in input().split()]
ans = (((n + a) - 1 ) // a) * (((m + a) - 1 ) // a)
print(ans)