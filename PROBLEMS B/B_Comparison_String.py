for _ in range(int(input())):
    n = int(input())
    s = list(input())
    ans = 1
    c = 1

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            c += 1
            ans = max(ans, c)
        else:
            c = 1

    print(ans + 1)  