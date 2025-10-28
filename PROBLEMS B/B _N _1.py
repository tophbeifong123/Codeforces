n,m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
flag = False
total = sum(arr)

for i in range(n):
    if total - arr[i] == m:
        flag = True
        break

if flag:
    print("Yes")    
else:
    print("No")