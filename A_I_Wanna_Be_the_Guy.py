n = int(input())
x = list(input().split())
y = list(input().split())
z = set(x[1::]) & set(y[1::])

if len(z) >= n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
