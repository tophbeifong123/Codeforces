for _ in range(int(input())):
    a,b,c,n = [int(x) for x in input().split()]
    check = max(a,b,c) - a + max(a,b,c) - b + max(a,b,c) - c
    if n >= check and (n - check) % 3 == 0:
        print("YES")
    else:
        print("NO")