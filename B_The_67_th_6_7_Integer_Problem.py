for _ in range(int(input())):
    a  = [int(x) for x in input().split()]
    print(-1*sum(a[0:-2]) + a[1])