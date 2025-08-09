n,k = [int(x) for x in input().split()]
yi = [int(x) for x in input().split()]
count = 0

for i in range(n):
    if k <= 5 - yi[i]:
        count += 1

print(count//3)