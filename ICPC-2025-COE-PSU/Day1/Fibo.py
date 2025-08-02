n = int(input())
a = 0
b = 1
result = 0
for i in range(n+1):
    if i == 0:
       result += a
    elif i == 1:
       result += b
    else:
       result += a +b
       a,b = b, a + b

print(result)