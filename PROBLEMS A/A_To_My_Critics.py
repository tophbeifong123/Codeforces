for _ in range(int(input())):
    lis = [int(x) for x in input().split()]
    lis.sort()
    if sum(lis[1:]) >= 10:
        print("YES")
    else:
        print("NO")