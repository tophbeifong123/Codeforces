for _ in range(int(input())):
    n = int(input())
    s = list(input())
    s.sort()

    if n != 5:
        print("NO")
        continue 
    print("YES") if s == ['T', 'i', 'm', 'r', 'u'] else print("NO")