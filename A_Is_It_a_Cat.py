for _ in range(int(input())):
    n = int(input())
    s = [x.lower() for x in list(input())]
    lis = []

    for i in range(n):
        if i == 0 or s[i] != s[i-1]:
            lis.append(s[i])

    if lis == ['m','e','o','w']:
        print("YES")
    else:
        print("NO")