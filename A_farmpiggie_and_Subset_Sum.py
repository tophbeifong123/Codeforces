for _ in range(int(input())):
    n = int(input())
    ans = [x for x in range(1,n+1)]

    ans = ans[1:] + ans[:1]
    print(*ans)