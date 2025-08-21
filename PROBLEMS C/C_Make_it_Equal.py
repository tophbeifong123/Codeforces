t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    cnt = {}
    for x in S:
        r = x % k
        c = r if r <= k - r else k - r
        cnt[c] = cnt.get(c, 0) + 1

    ok = True
    for x in T:
        r = x % k
        c = r if r <= k - r else k - r
        v = cnt.get(c, 0) - 1
        if v < 0:
            ok = False
            break
        cnt[c] = v

    print("YES" if ok else "NO")
