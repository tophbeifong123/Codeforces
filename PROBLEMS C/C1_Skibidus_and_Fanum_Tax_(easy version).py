for _ in range(int(input())):
    n,m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    flag_1 = True
    flag_2 = True

    arr = [ b[0] - x for x in a ]

    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i] = b[0] - a[i]
            if a[i] < a[i+1]:
                flag_1 = False
                break

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            flag_2 = False
            break

    if flag_1 or flag_2: print("YES")
    else: print("NO")