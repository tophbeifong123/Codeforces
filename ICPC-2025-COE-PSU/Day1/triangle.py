lis = []
for _ in range(int(input())):
    lis.append(int(input()))

lis.sort()
if len(lis) < 3:
    print("no")
else:    
    if lis[0] + lis[1] > lis[-1]:
        print("no")
    else:
        print("yes")
