try:
    x = input().strip()
    while True:
        a = int(x)
        print("input =", len(str(abs(a))))
        x = input().strip()
except:
    pass
