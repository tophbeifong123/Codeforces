n = int(input())
a = list(map(int, input().split()))

total = sum(a)

if total % 3 != 0:
    print(0)
else:
    target = total // 3
    prefix = 0
    count = 0
    ans = 0

    for i in range(n - 1):
        prefix += a[i]

        if prefix == 2 * target:
            ans += count

        if prefix == target:
            count += 1

    print(ans)