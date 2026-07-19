for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    
    one = a.count(1)
    two = a.count(2)

    if one % 2 == 0:
        two += one
    else:
        two += one - 1

    print("YES") if two % 2 == 0 else print("NO")