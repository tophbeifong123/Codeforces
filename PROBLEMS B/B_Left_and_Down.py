import math
for _ in range(int(input())):
    a, b, k = [int(x) for x in input().split()]
    g = math.gcd(a, b)
    if max(a//g, b//g) <= k:
        print(1)
    else:
        print(2)
