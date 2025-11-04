for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    result = 0
    count_even = 0
    count_odd = 0

    for i in range(n):
        if i % 2 == 0  and a[i] % 2 != 0:
            count_even += 1
        elif i % 2 != 0 and a[i] % 2 == 0:
            count_odd += 1

    if count_even == count_odd:
        print(count_even )
    else:
        print(-1)