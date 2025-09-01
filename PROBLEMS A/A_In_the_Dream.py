for _ in range(int(input())):
    a,b,c,d = [int(x) for x in input().split()]

    def ok(x,y):
        return max(x,y) <= 2*(min(x,y) +1)
    

    if ok(a,b) and ok(c-a,d-b):
        print("YES")
    else:
        print("NO")