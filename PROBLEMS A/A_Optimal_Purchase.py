for _ in range(int(input())):
    n,a,b = [int(x) for x in input().split()]
    ans = n // 3 * min(3 *a,b)

    if n % 3 == 2:
        ans += min(2 *a,b)
    elif n % 3 == 1:
        ans += min(a,b)

    print(ans)