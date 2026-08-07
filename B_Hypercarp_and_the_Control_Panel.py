# 1 1 2 3 3 2 2 1

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    c = 1
    b = []
    for i in range(n-1):
        if a[i] == a[i+1]:
            c += 1
        else:
            b.append((a[i], c))
            c = 1

    b.append((a[n-1], c))

    ans = len(b)
