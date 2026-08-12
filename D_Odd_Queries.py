for _ in range(int(input())):
    n,q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    prefix = [0]

    for i in a:
        prefix.append(prefix[-1] + i)

    for _ in range(q):
        l,r,k = [int(x) for x in input().split()]
        ans = prefix[n] - prefix[r] - prefix[l-1]  + (r - l + 1) * k
 
        if ans % 2 == 1:
            print('YES')
        else:
            print('NO')