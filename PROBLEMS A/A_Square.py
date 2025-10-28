for _ in range(int(input())):
    arr = list(input().split())
    if len(set(arr)) == 1:
        print("YES")
    else:
        print("NO")