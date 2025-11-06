n = int(input())
arr = [int(x) for x in input().split()]
m = 1
count = 1

for i in range(n-1):
    if arr[i] < arr[i+1]:
        count += 1
        m = max(m, count)
    else:
        count = 1

print(m)