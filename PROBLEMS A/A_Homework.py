for _ in range(int(input())):
    n = int(input())
    a = list(input())
    m = int(input())
    b = list(input())
    c = list(input())


    for i in range(m):
        if c[i] == "D":
            a.append(b[i])
        else:
            a.insert(0, b[i])

    print("".join(a))



