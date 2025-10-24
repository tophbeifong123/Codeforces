for _ in range(int(input())):
    n,a,b = [int(x) for x in input().split()]
    if a < b / 2:
        print(n*a)
    else:
        print(n//2 * b) if n%2 == 0 else print(n//2 * b + a)