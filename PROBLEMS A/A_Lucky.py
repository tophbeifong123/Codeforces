for _ in range(int(input())):
    x = list(input())
    x = [int(i) for i in x]

    if sum(x[0:3]) == sum(x[3:6]):
        print("YES")
    else:
        print("NO")