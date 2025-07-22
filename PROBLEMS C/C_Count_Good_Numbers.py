for _ in range(int(input())):
    l,r = [int(x) for x in input().split()]
    count = 0
    for i in range(l,r+1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            count +=1
    print(count)