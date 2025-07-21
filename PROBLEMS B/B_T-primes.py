import math
n = int(input())
lis = [int(x) for x in input().split()]

def prime(n):
    if n < 2 :
        return False
    if n == 2:
        return True
    if n % 2 == 0:  
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

for i in lis:
    root = math.isqrt(i)
    if root * root == i and prime(root):
        print("YES")
    else:
        print("NO")