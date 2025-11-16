for _ in range(int(input())):
    a,b,n = [int(x) for x in input().split()]
    flag1 = True
    leghth1 = min(b,a/n)
    if b <= a / n or a == b:
        print(1)
    else:
        print(2)