for _ in range(int(input())):
    a,b,c = [int(x) for x in input().split()]
    if a == b:
        if c % 2 == 0:
            print("Second")
        else:
            print("First")
    elif a > b:
        print("First")
    else:
        print("Second")