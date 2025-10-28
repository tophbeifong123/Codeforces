for _ in range(int(input())):
    n = int(input())
    s,t = [list(x) for x in input().split()]
    if sorted(s) == sorted(t):
        print("YES")
    else:
        print("NO")