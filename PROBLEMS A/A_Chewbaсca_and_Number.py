import sys
input = sys.stdin.readline

n = list(input().strip())

if int(n[0]) >= 5 and n[0] != "9":
    print(9-int(n[0]),end="")
else:
    print(n[0],end="")

for i in n[1::]:
    if int(i) >= 5:
        print(9-int(i),end="")
    else:
        print(i,end="")