n = int(input())
lis = [int(x) for x in input().split()]

s = 0
d = 0

for i in range(n):
    if i % 2 ==0:
        if lis[0] > lis[-1]:
            s += lis[0]
            lis.pop(0)
        else:
            s += lis[-1]
            lis.pop(-1)
    else:
        if lis[0] > lis[-1]:
            d += lis[0]
            lis.pop(0)
        else:
            d += lis[-1]
            lis.pop(-1)

print(s,d)