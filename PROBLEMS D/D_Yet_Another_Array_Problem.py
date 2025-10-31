import sys,math
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    flag = False
    result = 0
    
    
    for i in range(2,max(a)+10):
        if any(math.gcd(i,x) == 1 for x in a):
            flag = True
            result = i
            break

    if flag:print(result)
    else:print(-1)