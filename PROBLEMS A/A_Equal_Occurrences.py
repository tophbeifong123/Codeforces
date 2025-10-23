from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)

    ans = 0
    for k in range(1, max(freq.values())+1):
        m = sum(1 for v in freq.values() if v >= k)
        ans = max(ans, m * k)
    print(ans)
