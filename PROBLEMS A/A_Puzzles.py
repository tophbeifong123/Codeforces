n, m = map(int, input().split())
f = sorted(map(int, input().split()))
lis = []
for i in range(m-n + 1):
    lis.append(f[n-1 + i] - f[i])


print(min(lis))