for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    if k in a:
        print("YES")
    else:
        print("NO") 