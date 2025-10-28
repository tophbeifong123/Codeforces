import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,a,b,c = [int(x) for x in input().split()]
    day = 0
    while n > 0:
        print('n:', n, 'day:', day)
        if n >= a+b+c:
            n -= a+b+c
            day += 3
        elif n >= a+b:
            n -= a+b
            day += 2
        elif n >= a:
            n -= a
            day += 1
    print(day)