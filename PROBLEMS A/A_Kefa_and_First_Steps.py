n = int(input())
a = [int(x) for x in input().split()]
count = 1
m = 1
for i in range(n-1):
    if a[i+1] >= a[i]:
        count +=1
        if count > m:
            m = count
    else:
        count = 1

print(m)