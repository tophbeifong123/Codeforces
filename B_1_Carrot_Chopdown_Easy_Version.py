from collections import *
from bisect import *

for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    c = Counter(a)
    a.sort()
    ans = 0

    for target in range(1, m + 1):
        p = bisect_left(a, target)
        current = n - p
        current += c[2 * target]
        ans = max(ans, current)

    print(ans)