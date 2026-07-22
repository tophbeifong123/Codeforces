for _ in range(int(input())):
    n = int(input())
    s = sorted([int(x) for x in input().split()])

    diff = s[1] - s[0]

    for i in range(n - 1):
        diff = min(diff,(s[i+1] - s[i]))


    print(diff)