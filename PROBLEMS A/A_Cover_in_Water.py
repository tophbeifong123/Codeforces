for _ in range(int(input())):
    n = int(input())
    s = list(input())
    flag = 0
    count = 0
    m = 0
    for i in s:
        if i == '.':
            count += 1
            flag =  max(flag,count)
            m += 1
        else:
            count = 0

    if flag >= 3:
        print(2)
    else:
        print(m)
