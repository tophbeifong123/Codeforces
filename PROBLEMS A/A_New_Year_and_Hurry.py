n,k = [int(x) for x in input().split()]
count = 0
for i in range(1,n+1):
    k += 5 * i
    if 240 - k >= 0:
        count += 1


print(count)