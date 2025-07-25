x1,x2,x3,x4 = [int(x) for x in input().split()]
abc = max(x1,x2,x3,x4)
lis = []

for i in [x1,x2,x3,x4]:
    lis.append(abc -i)

lis.sort(reverse=True)
print(*lis[0:-1])