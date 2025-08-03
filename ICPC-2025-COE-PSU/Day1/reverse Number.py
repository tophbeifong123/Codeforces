try:
    while True:
        n = input()
        while int(n) % 10 == 0:
            n = int(n) // 10
        print(str(n)[::-1])
except :
    pass