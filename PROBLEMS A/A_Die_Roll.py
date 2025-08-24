y,w = [int(x) for x in input().split()]
a = 6 - max(y,w) + 1 

if a == 0:
    print("0/1")
elif a == 1:
    print("1/6")
elif a == 2:
    print("1/3")
elif a == 3:
    print("1/2")
elif a == 4:
    print("2/3")
elif a == 5:
    print("5/6")
elif a == 6:
    print("1/1")