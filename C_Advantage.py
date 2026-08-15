for _ in range(int(input())):
    n = int(input())
    s = [int(x) for x in input().split()]

    m = sorted(s)

    for i in s:
        if i - m[-1] == 0:
            print(i - m[-2],end=' ')
        else:
            print(i - m[-1],end=' ')
    print()