n,l = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])
flag = 0

if 0 not in a or l not in a:
    flag = max(a[0], l - a[-1])

for i in range(n-1):
    if (a[i+1] - a[i]) / 2 > flag:
        flag = (a[i+1] - a[i]) / 2

print(f'{flag:.10f}')