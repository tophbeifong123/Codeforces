dp = {}

for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    flag = True
    for i in arr:
        if i in dp:
            dp[i] += 1
        else:
            dp[i] = 1
    
    print(dp)