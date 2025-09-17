for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    if k == 1 and len(set(a)) != 1 and a != sorted(a):
        print("NO")
    else:
        print("YES")