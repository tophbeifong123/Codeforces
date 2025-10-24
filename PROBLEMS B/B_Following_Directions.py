for _ in range(int(input())):
    n = int(input())
    a = list(input())
    x, y = 0, 0
    flag = False
    for i in a:
        if i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
        elif i == 'U':
            y += 1
        else:
            y -= 1
        if x == 1 and y == 1:
            flag = True
            break
    print("YES" if flag else "NO")