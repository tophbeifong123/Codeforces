import sys
input = sys.stdin.readline
for i in range(int(input())):
    n =  int(input())
    arr = list(map(int, input().split()))
    c = list(map(int, input().split()))
    if len(set(arr)) == 1 or len(arr) == 1:
        print(0)
    else:
        dp = [0]*n
        ans = 0
        for i in range(n):
            dp[i] = c[i]
            for j in range(i):
                if arr[j] <= arr[i]:
                    dp[i] = max(dp[i], dp[j] + c[i])
            ans = max(ans, dp[i])
        total = sum(c)  
        print(total - ans)