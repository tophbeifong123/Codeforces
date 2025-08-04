import bisect

n = int(input())
xi = [int(x) for x in input().split()]
xi.sort()

q = int(input())
mi = [int(input()) for _ in range(q)]

for money in mi:
    count = bisect.bisect_right(xi,money)
    bisect.insort_right(xi,money)
    print(xi)
    print(count)
