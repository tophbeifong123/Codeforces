n = int(input())
lis = [int(x) for x in input().split()]

max_point = lis[0]
min_point = lis[0]
count = 0

for i in range(1,n):
    if lis[i] > max_point:
        max_point = lis[i]
        count += 1
    if lis[i] < min_point:
        min_point = lis[i]
        count +=1

print(count)