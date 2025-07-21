n = int(input())
a = [int(x) for x in input().split()]

flag = 0
crime = 0
for i in range(n):
    if a[i] > 0:
        flag += a[i]
    else:
        if flag > 0:
            flag -= 1
        else:
            crime +=  1

print(crime)