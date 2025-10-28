import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,q = [int(x) for x in input().split()]
    s = input()
    a = [int(x) for x in input().split()]
    for i in range(q):
        count = 0
        if s.count('B') == 0:
            print(a[i])
        else:
            while a[i] > 0:
                for j in range(n):
                    if a[i] <= 0:
                        break
                    elif s[j] == 'B':
                        a[i] = a[i] // 2 
                    elif s[j] == 'A': 
                        a[i] = a[i]  -1 
                    count += 1  
            print(count)
            