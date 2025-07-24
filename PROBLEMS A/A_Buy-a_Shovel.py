k,r = [int(x) for x in input().split()]
count = 0
while True:
    count += 1
    if k*count % 10 == 0 or (k*count - r)%10 == 0 :
        break

print(count)