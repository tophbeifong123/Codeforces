lis = [5,5,5,5,5,5,1,2,3,4,5]

for i in range(len(lis)):
    c = 0
    for j in range(len(lis)):
        if lis[i] == lis[j]:
            c +=1
    if c > len(lis)/2:
        print("YES")
        exit()
print("NO")