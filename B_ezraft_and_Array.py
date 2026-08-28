for _ in range(int(input())):
    n = int(input())

    ans = [1,2,3]

    if n == 1:
        print(1) 
    elif n == 2:
        print(-1)
    else:
        for i in range(n - 3):
            ans.append(sum(ans))
        print(*ans)