dp = {}

for _ in range(int(input())):
    a,b = input().split()
    b = int(b)
    if a in dp:
        dp[a] += b
    else:
        dp[a] = b

print(max(dp), dp[max(dp)])