for _ in range(int(input())):
    n,s,x = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    if (s -  sum(a)) % x == 0 and s - sum(a) >= 0 :
        print('YES')
    else:
        print('NO')