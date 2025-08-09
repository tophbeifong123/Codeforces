n = int(input())
lis = []

while len(lis) < n:
    x = [int(x) for x in input().split()]
    lis.extend(x)

max_point = lis[0]
max_restult = lis[0]

for i in lis[1:]:
    max_point = max(i, max_point + i)
    max_restult = max(max_restult, max_point)

print(max_restult)