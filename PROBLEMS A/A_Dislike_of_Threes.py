lis = []
for i in range(1,1667):
    if i % 3 != 0 and i % 10 != 3:
        lis.append(i)

for _ in range(int(input())):
    k = int(input())

    print(lis[k-1])