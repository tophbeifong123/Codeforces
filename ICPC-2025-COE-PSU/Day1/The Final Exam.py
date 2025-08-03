x = int(input())
a1,a2,a3,a4,a5 = [int(x) for x in input().split()]

if a1 + a2 + a3 + a4 + a5 == x:
    print(a1,a2,a3,a4,a5)
elif 0 + a2 + a3 + a4 + a5 == x:
    print(0,a2,a3,a4,a5)
elif a1 + 0 + a3 + a4 + a5 == x:
    print(a1,0,a3,a4,a5)
elif a1 + a2 + 0 + a4 + a5 == x:
    print(a1,a2,0,a4,a5)
elif a1 + a2 + a3 + 0 + a5 == x:
    print(a1,a2,a3,0,a5)
elif a1 + a2 + a3 + a4 + 0 == x:
    print(a1,a2,a3,a4,0)
else:
    print(-1)