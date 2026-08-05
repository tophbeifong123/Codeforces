for _ in range(int(input())):
    a = [int(x) for x in input().split()]
    a.sort()
    ans = min(max(a) - a[1],(a[1] - a[0]))
    if a[0] == a[1]:
        print(0)
    else:
        print(ans)

