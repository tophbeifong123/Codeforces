
for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        a = list(input())
        arr.append(a.index('#') + 1)

    print(*arr[::-1])