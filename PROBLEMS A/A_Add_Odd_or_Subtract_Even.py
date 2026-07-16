for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    diff = abs(a - b)

    if a == b:
        print(0)
    elif a > b:
        if diff % 2 != 0 :
            print(2)
        else:
            print(1)
    else:
        if diff % 2 == 0 :
            print(2)
        else:
            print(1)
