for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    if b > a:
        print(b-a)
    else:
        i = 1
        while True:
            if b*i > a:
                print(a - b*i)
                break
            i+=1