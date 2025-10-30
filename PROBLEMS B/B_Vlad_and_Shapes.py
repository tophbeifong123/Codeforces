for _ in range(int(input())):
    n = int(input())
    col = []
    row = 0
    for i in range(n):
        s = list(input())
        if '1' in s:
            row += 1
            col.append(s.count('1'))

    if row == col[0] and len(set(col)) == 1:print("SQUARE")
    else:print("TRIANGLE")
        