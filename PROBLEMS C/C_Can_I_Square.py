import math
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if math.sqrt(sum(arr)).is_integer():
        print("YES")
    else:
        print("NO")