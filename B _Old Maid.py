from collections import *


n = int(input())
a = [int(x) for x in input().split()]
count = Counter(a)
ans = 0

for i,l in count.items():
    if l % 2 == 1:
        ans += i


print(ans)