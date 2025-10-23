lisA = [[int(x) for x in input().split()] for _ in range(3)]
lisB = [[1,1,1],[1,1,1],[1,1,1]]

dirs = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]

for i in range(3):
    for j in range(3):
        if lisA[i][j] % 2 != 0:
            for dx,dy in dirs:
                x,y = i+dx, j+dy
                if 0 <= x < 3 and 0 <= y < 3:   # กัน out of range
                    lisB[x][y] ^= 1              # toggle ด้วย XOR

for row in lisB:
    print(''.join(map(str,row)))
