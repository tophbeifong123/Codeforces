for _ in range(int(input())):
    n = int(input())
    s = list(input())

    ans = 1

    for i in range(n -1):
        if s[i] == '<' and s[i+1] != '>':
            ans += 1
        elif s[i] == '>' and s[i+1] != '<':
            ans += 1

    if n % 2 == 0:
        print(ans)
    else:
        print(ans + 1)
