from collections import Counter 
n = int(input())
arr = [int(x) for x in input().split()]
count = Counter(arr)
A = 0
B = []

for i in count:
    if count[i] ==1:
        A += 1
    else:
        B.append(count[i])

result = 1
for i in B:
    result *= i

if len(set(arr)) == 1:
    print(0)
else:
    if A == 0: print(result) 
    else: print(result * A)