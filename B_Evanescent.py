for _ in range(int(input())):
    n = int(input())
    s = input()

    block = 1

    for i in range(n-1):
        if s[i] != s[i+1]:
            block += 1


    dec = 0

    for i in range(1,n-1):
        if s[i] != s[i+1] and s[i] != s[i-1]:
            if s[i-1] == s[i+1]:
                dec = 2
                break
            else:
                dec = 1
           
    print(block - dec)