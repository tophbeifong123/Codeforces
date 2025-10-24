n,t = [int(x) for x in input().split()]
flag = -1
for i in range(10**(n-1),10**n):
    if i%t == 0:
        flag = i
        break
print(flag)