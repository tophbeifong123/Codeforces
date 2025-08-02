d,n = [int(x) for x in input().split()]
count = 0
for i in range(1, n + 1):
    if str(d) in str(i):
        count += 1

print(count)