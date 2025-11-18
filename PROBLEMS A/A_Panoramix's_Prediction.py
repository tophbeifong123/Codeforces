def is_prime(num):
    if num < 2 or num % 2 == 0:
        return False
    i = 3 
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

n,m = [int(x) for x in input().split()]
flag = True

for i in range(n+1,m):
    if is_prime(i):
        flag = False
        break

if flag and is_prime(m):
    print("YES")
else:
    print("NO")