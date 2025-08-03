for _ in range(int(input())):
    s = list(input())
    w = "codeforces"
    count = 0
    for i in range(len(s)):
        if s[i] != w[i]:
            count += 1
    print(count)