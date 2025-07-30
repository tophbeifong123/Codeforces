for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    flag = True

    for i in range(n-1):
        if a[i + 1] - a[i] > 1:
            flag = False
            break
    
    print("YES" if flag else "NO")