x1,x2,x3 = [int(x) for x in input().split()]
point = 0

if x1 > x2 and x1 < x3 or x1 < x2 and x1 > x3:
    point = x1
elif x2 > x1 and x2 < x3 or x2 < x1 and x2 > x3:
    point = x2
else:
    point = x3

print(int(abs(x1 - point) + abs(x2 - point) + abs(x3 - point)))