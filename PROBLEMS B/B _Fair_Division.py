for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    one = a.count(1)
    two = a.count(2)
    total = one + (two * 2 )

    if total % 2 != 0:
        print("NO")
    elif two % 2 != 0 and one == 0:
        print("NO")
    else:
        print("YES")