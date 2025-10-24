n,m = [int(x) for x in input().split()]
start,stop = int(n / 2 + n % 2)  , n
if m > n:
     print(-1)
else:
    for i in range(start, stop+1):
        if i % m == 0:
            print(i)
            break
