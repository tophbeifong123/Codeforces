import sys

n = int(input())

row = 0
col = 0

for i in range(1, n+1):
    print("c", i, i)
    sys.stdout.flush()
    check = input()
    if check == "yes":
        row = i
        col = i
#1 1 2 2 3 3
k = 0
for j in range(1, n+1):
    for i in range(1, n+1):
        if i == j:
            continue
        print("c", j, i)
        sys.stdout.flush()
        # 1 2 2 3 3 4
        check = input()
        if check == "yes":
            col = i
            k = 1
            break
    if k == 1:
        break
        
print("d", row, col)
sys.stdout.flush()