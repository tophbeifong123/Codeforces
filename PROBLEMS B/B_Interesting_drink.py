n = int(input())
x = [int(x) for x in input().split()]
q = int(input())
m = []
for _ in range(q):
    m.append(int(input()))
count =0
for i in m:
    count = 0
    for j in x:
        if i >= j:
            count += 1
    print(count)