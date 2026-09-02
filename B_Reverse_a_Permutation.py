for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    for i in range(n):
        target = n - i

        if p[i] != target:
            j = p.index(target)
            p[i:j + 1] = p[i:j + 1][::-1]
            break

    print(*p)