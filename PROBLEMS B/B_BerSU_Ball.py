n = int(input())
a = sorted([int(x) for x in input().split()])
m = int(input())
b = sorted([int(x) for x in input().split()])

ans = 0

for i in a:
    for j in b:
        if abs(i - j) <= 1:
            b.remove(j)
            ans += 1
            break

print(ans)