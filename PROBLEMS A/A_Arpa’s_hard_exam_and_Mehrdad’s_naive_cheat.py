n = int(input())
check = n % 4 
if n == 0:
    print(1)
else:
    if check == 1:
        print(8)
    elif check == 2:
        print(4)
    elif check == 3:
        print(2)
    else:
        print(6)