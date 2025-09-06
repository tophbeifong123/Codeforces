for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    total = sum(a)
    if total % 2 == 0:
        print("YES")
    else:
        print("NO")