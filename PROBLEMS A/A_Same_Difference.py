for _ in range(int(input())):
    n = int(input())
    s = list(input())
    count = 0
    for i in s[::-1]:
        if i == s[-1]:
            count += 1

    print(n - count)