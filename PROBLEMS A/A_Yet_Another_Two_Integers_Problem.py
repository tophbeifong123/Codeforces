for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    c = abs(a - b)
    count = 0
    if a == b:
        print(0)
    else:
        print( c//10 ) if  c%10 == 0 else print( c//10 + 1 )