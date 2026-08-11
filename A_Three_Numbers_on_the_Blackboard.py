for _ in range(int(input())):
    a = sorted([int(x) for x in input().split()])

    if a[0] + a[1] < a[-1]:
        print(a[1])
    else:
        print(a[-1] - a[0])