for _ in range(int(input())):
    a,b,n = [int(x) for x in input().split()]
    count = 0
    while n >= a or n >= b:
        if a > b:
            b += a
            count += 1
        else:
            a += b
            count += 1
    print(count - 1)