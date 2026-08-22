for i in range(int(input())):
    n = input()
    n = n[::-1]
    ans = []

    for i in range(len(n)):
        if int(n[i]) > 0:
            ans.append(n[i]+'0'*i)

    print(len(ans))
    print(*ans)