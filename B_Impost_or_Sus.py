for _ in range(int(input())):
    r = list(input())
    ans = 0

    if r[0] == 'u':
        r[0] = 's'
        ans += 1

    if r[-1] == 'u':
        r[-1] = 's'
        ans += 1

    for i in range(len(r) - 1):
        if r[i] == 'u' and r[i+1] == 'u':
            r[i+1] = 's'
            ans += 1
            
    print(ans)