for _ in range(int(input())):
    x = int(input())
    k = 3 
    i = 2
    while True:
        if x % k == 0:
            print(x // k)
            break
        i *= 2
        k = k + i