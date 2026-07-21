for _ in range(int(input())):
    n = int(input())
    s = list(input())
    
    l = 0

    for i in s:
        if i == '(':
            l += 1
        else:
            if l <= 0:
                l = 0
            else:
                l -= 1
        
    print(l)