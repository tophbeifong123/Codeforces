n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
flag = 1
c = 0

for i in a:
    if flag < i:
        c += i - flag
        flag  = i
    elif flag == i:
        pass
    else:
        c += n - flag + i 
        flag = i

print(c) 