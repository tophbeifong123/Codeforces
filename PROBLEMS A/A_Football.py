dp = {}

for _ in range(int(input())):
    a = input()
    if a in dp:
        dp[a] += 1
    else:
        dp[a] = 1

print(max(dp,key=dp.get))