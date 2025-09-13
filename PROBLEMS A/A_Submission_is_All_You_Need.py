import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if n == 1:
        if s[0] == 0:
            print(1)
        else:
            print(s[0])
    else:
        print(s[-1] + s[-2] + 1)
