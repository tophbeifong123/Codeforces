Min = float('inf')
Min = float('inf')
for i in range(int(input())):
    n = int(input())
    if i == 0:
        Max = n
    if n > Max:
        Max = n
    elif n < Min:
        Min = n

print(Max)
print(Min)