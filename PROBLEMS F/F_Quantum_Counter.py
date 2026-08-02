a,b = [int(x) for x in input().split()]
ans = 0

for i in range(a-1):
    
    
    if a % b ==0 :
        print(f'{a} % {b}')
        ans += 1
        
    a -= 1
    b += 1

print(ans)