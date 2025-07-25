a,b = [int(x) for x in input().split()]
m = min(a,b)
n = max(a,b)

print(m, (n - m) //2)