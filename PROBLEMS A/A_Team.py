ans = 0
for _ in range(int(input())):
    s = list(input())
    if s.count('1') >= 2 :
        ans += 1 


print(ans) 