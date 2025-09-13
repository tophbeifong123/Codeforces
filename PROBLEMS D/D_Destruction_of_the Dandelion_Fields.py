import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    odds = [x for x in a if x % 2 == 1]
    evens = [x for x in a if x % 2 == 0]

    if not odds:           
        print(0)
        continue

    odds.sort(reverse=True)
    take = (len(odds) + 1) // 2         
    ans = sum(evens) + sum(odds[:take]) 
    print(ans)
