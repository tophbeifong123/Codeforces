a1,a2,a3,a4 = [int(x) for x in input().split()]
s = list(input())
point = 0 

for i in s:
    if i == "1":
        point += a1 
    elif i == "2":
        point += a2 
    elif i == "3":        
        point += a3 
    else:
        point += a4 

print(point)