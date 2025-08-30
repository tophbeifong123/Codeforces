import math

for _ in range(int(input())):
    n = int(input())
    a =  sorted([int(x) for x in input().split()])

    a[0] += 1
    print(math.prod(a))