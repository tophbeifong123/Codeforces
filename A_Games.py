lis = []
for _ in range(int(input())):
    h,a = [int(x) for x in input().split()]
    lis.append((h,a))

count = 0
for i in range(len(lis)):
    for j in range(len(lis)):
        if lis[i][1] == lis[j][0]:
            count += 1

print(count)