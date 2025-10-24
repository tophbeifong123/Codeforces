for _ in range(int(input())):
    a = int(input())
    if 360 / (180 - a) == int(360 / (180 - a)):
        print("YES")
    else:
        print("NO")