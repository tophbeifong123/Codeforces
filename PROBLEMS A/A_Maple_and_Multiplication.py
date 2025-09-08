for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    if a == b:
        print(0)
    elif a == 1 or b == 1:
        print(1)
    else:
        print(2)