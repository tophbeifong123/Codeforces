for _ in range(int(input())):
    s = [int(x) for x in input().split()]
    if max(s[0],s[1]) in sorted(s)[-2:] and max(s[2],s[3]) in sorted(s)[-2:]:
        print("YES")
    else:
        print("NO")
