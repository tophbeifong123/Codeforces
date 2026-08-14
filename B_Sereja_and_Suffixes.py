n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

suffix = [0] * n
seen = set()

for i in range(n-1,-1,-1):
    seen.add(a[i])
    suffix[i] = len(seen)

for i in range(m):
    l = int(input())
    print(suffix[l - 1])