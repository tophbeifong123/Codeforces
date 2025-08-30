for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    count = 1
    if n == 1:
        print("YES")
        continue
    else:
        for i in range(n-1):
            if a[i+1] - a[i] > 0:
                count += 1
            
        if count == n:
            print("YES")
        else:
            print("NO")