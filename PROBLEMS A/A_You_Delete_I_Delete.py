for _ in range(int(input())):
    s = list(input())
    flag_0 = False
    flag_1 = False
    ans = ''

    for i in s:
        if i == '0' and flag_0 == False :
           flag_0 = True
        elif  i == '1' and flag_1 == False:
            flag_1 = True
        else:
            ans += i

    print(ans) 