for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    arr = sorted([int(x) for x in input().split()])
    even ,odd = [],[]
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)