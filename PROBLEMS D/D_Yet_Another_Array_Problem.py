import sys,math
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    flag = False
    x = 2
    
    if 1 in arr:
        x = 2
        flag = True
    else:
        for i in range(2,max(arr)+1):
            if any(math.gcd(i,x)==1 for x in arr):
                flag = True
                x = i
                break

    if flag:print(x)
    else:print(-1)
    
    