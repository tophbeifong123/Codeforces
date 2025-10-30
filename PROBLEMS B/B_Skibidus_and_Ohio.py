for _ in range(int(input())):
    s = list(input())
    flag = len(s)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            flag = 1
            break
    
    print(flag)