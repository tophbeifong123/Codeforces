n,m = [int(x) for x in input().split()]
for i in range(n):
    if i < m:
        print("OK")
    else:
        print("Too Many Requests")