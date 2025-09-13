for _ in range(int(input())):
    x,n = [int(x) for x in input().split()]

    if n % 2 == 0:
        print(0)
    else:
        print(x)