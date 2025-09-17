for _ in range(int(input())):
    n = int(input())
    count = 0
    point = 0

    while n != 1:
        point += 1 
        if n % 6 == 0:
            n //= 6
            count = 0
        else:
            n *= 2
            count+= 1
            if count == 2:
                break
    

    if count == 2:
        print(-1)
    else:
        print(point)