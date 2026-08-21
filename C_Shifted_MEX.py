for _ in range(int(input())):
    n = int(input())
    a = sorted(set([int(x) for x in input().split()]))

    ans = 1
    current = 1

    for i in range(len(a) - 1):
        if a[i+1] - a[i] == 1:
            current += 1
        else:
            current = 1

        ans = max(ans,current)

    print(ans)