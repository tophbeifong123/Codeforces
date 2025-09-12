import sys
import bisect

input = sys.stdin.readline

for _ in range(int(input())):
    n,c = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    T = c
    ans = 0

    for _ in range(n):
        idx = bisect.bisect_right(a,T) - 1
        if idx >= 0:
            a.pop(idx)
        else:
            ans += 1
            a.pop(0)
        T//=2 

    print(ans)