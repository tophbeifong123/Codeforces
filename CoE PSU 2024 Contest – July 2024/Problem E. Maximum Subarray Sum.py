lis = []
n = int(input())
while len(lis) < n:
    x = [int(x) for x in input().split()]
    lis.extend(x)
m = 0
for i in range(n):
    for j in range(i,n+1):
        if sum(lis[i:j]) > m:
            m = sum(lis[i:j])

print(m)