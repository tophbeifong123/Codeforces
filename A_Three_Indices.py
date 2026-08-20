for i in range(int(input())):
    n = int(input())
    p = [int(x) for x in input().split()]

    ok = False

    for j in range(1,n-1):
        if p[j-1] < p[j] and p[j] > p[j+1]:
            print('YES')
            print(j ,j + 1,j + 2)
            ok = True
            break


    if not ok:
        print('NO')