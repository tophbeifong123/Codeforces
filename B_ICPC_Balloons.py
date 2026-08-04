for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    flag = []

    for i in s:
        if i not in flag:
            ans += 2
            flag.append(i)
        else:
            ans += 1

    print(ans)