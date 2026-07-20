for _ in range(int(input())):
    a,b,c = [int(x) for x in input().split()]

    for i in range(5):
        if a <= b  and a <=c:
            a += 1
        elif b <=a and b <=c:
            b += 1
        elif c <=a and c <=b:
            c += 1

    print(a*b*c)

