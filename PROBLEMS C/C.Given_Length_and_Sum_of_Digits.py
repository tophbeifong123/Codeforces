m, s = [int(i) for i in input().split()]
lis = []
tmp = s
a = 0
b = 0

if tmp%m != 0:
    tmp = s//m
    a = tmp+1
    b = tmp
else:
    tmp = s//m
    a = tmp+1
    b= tmp-1
print(a,b)

# 2
# 10 11
# 10 12

# 10 11 12
# 9 10 12 13