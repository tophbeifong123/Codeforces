x1,y1 = [int(x) for x in input().split()]
x2,y2 = [int(x) for x in input().split()]
x3,y3 = [int(x) for x in input().split()]

bx = -x3 + x1 + x2
ax = 2*x1 - bx
cx = 2*x3 - ax

by = -y3 + y1 + y2
ay = 2*y1 - by
cy = 2*y3 - ay

print(ax,ay)
print(bx,by)    
print(cx,cy)