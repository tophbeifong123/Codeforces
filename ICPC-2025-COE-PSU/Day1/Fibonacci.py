n = int(input())
a = 0
b = 1
for i in range(n):
    if i == 0:
        print(a,end=" ")    
    elif i == 1:
        print(b,end=" ")
    else:
        print(a + b,end=" ")
        a,b = b, a + b