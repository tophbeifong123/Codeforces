n = int(input())
a = [int(x) for x in input().split()]

m = max(a)
result = 0 
for i in a:
    result += m - i

print(result)