n,m = [int(x) for x in input().split()]

ans1 = (m // 2 + (m % 2)) * 2 
ans1 += m - ans1

ans2 = n - (m // 2 + (m % 2))
ans2 += 1

if n > m:
    print(n - m)
else:
    if n == 1:
        print(ans1)
    else:
        print(ans2)