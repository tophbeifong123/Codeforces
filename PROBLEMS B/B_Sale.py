n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
price = 0
count = 0
for i in range(n):
    if a[i] < 0:
        price+= abs(a[i])
        count +=1
        if count >= m:
            break

print(price)
