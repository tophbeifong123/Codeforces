for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = sorted(a)

    for i in range(n):
        if a[i] != b[1]:
            print(i + 1)
            break