for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    if n == 1 or  a != sorted(a):
        print(1)
    else:
        print(len(a))

