import math
for _ in range(int(input())):
    n,x = [int(x) for x in input().split()]
    if n <= 2:
        print(1)
    else:
        print(math.ceil((n-2)/ x) + 1) 