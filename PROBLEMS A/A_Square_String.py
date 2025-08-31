for _  in range(int(input())):
    s = list(input())

    if s[0:len(s)//2] == s[len(s)//2:]:
        print("YES")
    else:
        print("NO")