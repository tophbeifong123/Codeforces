a,b = [int(x) for x in input().split()]
result = 0
for i in range(a, b + 1):
    result += i

print(result)