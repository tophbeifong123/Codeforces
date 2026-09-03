import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    s = input()

    if k > n / 2 :
        print(-1)
        continue

    ans = 0

    for i in range(k):
        if s[i] != 'R':
            ans += 1

        if s[n - i - 1] != 'L':
            ans += 1

    print(ans)