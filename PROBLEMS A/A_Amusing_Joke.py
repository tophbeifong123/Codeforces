a = list(input())
b = list(input())
c = sorted(list(input()))

x = a + b
x.sort()

if x == c:
    print("YES")
else:
    print("NO") 