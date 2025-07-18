n = int(input())
lis = [int(x) for x in input().split()]

even = []
odd = []

for i in range(n):
    if lis[i] % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

if len(even) == 1:
    print(even[0] + 1)
else:
    print(odd[0] + 1)
    