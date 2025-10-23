col_x = 0
col_y = 0
col_z = 0
for _ in range(int(input())):
    x,y,z = [int(x) for x in input().split()]
    col_x += x
    col_y += y
    col_z += z

if col_x == 0 and col_y == 0 and col_z == 0:
    print("YES")
else:
    print("NO")