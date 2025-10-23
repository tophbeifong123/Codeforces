matrix = []
for i in range(5):
    row = [int(x) for x in input().split()]
    matrix.append(row)

result = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            result = abs(2 - i) + abs(2 - j)
            break

print(result)   