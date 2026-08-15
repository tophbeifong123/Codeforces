from collections import *

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

ans1,ans2 = 0,0

ans1 = Counter(a) - Counter(b)
ans2 = Counter(b) - Counter(c)


print(*ans1)
print(*ans2)