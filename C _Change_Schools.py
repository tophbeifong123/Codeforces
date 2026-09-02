from collections import *

n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
count  = Counter(a)

mx = count.most_common(1)[0][1]
ans = 0

for i,l in count.items():
    if l + 1 >= mx:
        ans += 1


print(ans)