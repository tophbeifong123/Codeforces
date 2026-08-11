for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    cnt = {}
    ans = 0

    for i in range(n):
        x = a[i] - i

        ans += cnt.get(x,0)

        cnt[x] = cnt.get(x,0) + 1

    print(ans)