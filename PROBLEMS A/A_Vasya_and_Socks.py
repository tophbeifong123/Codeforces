n,m = [int(x) for x in input().split()]
day = 0
result = 0
while True:
    day += 1
    result += 1
    n -= 1
    if day % m == 0:
        n += 1
        day = 0
    if n == 0:
        break

print(result)