n,m = [int(x) for x in input().split()]
ans = 0

while m > n:
    if m % 2 == 0:
        m = m // 2
    else:
        m += 1 
    ans += 1


print(ans + (n - m))