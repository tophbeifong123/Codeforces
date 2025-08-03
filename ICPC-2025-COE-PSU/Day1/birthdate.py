try:
    lis = []
    while True:
        line = input().strip()
        a, b, c, d = line.split()
        lis.append((a, int(b), int(c), int(d)))
except:
    lis.sort(key=lambda x: x[0])
    lis.sort(key=lambda x: x[1])
    lis.sort(key=lambda x: x[2])
    lis.sort(key=lambda x: x[3])
    print(lis[-1][0])
    print(lis[0][0])
