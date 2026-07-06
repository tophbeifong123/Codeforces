n = int(input())
h = 1
c = 1
b = c 

if n < 4:
    print(1)
else:
    while True:
        if n > b:
            n -= b
            h += 1
            c += 2
            b += c
        else:
            break

    print(h)