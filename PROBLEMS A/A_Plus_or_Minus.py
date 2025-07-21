for _ in range(int(input())):
    a,b,c = [int(x) for x in input().split()]
    if a + b == c:
        print('+')
    else:
        print('-')