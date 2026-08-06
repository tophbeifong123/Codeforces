from collections import *

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    ans = sum(a)
    c = Counter(a)
    M,m = c.most_common(1)[0]
    o = n - m

    if o >= m - 1:
        print(ans)
    else:
        print(ans - (M*m) + M*(o+2))