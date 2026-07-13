m = []

for i in range(5):
    l = [int(x) for x in input().split()]
    m.append(l)

for i in range(5):
    for l in range(5):
        if m[i][l] == 1:
            print(abs(i - 2) + abs(l - 2))
            break

