n,t = [int(i) for i in input().split()]
lis = []
for _ in range(t):
    a,b = input().split()
    lis.append((int(a),b))


lis.sort(key=lambda x: x[0],reverse=True)

price = 0
for i, name in lis[:n]:
    price += i

print(price)
for i in lis[n:0]:
    print(i[1])