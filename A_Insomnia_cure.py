k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

if k == 1 or l == 1 or m == 1 or n == 1:
    print(d)
    exit()

lis = filter(lambda x: x%k != 0, range(1, d + 1))
lis = filter(lambda x: x%l != 0, lis)
lis = filter(lambda x: x%m != 0, lis)
lis = filter(lambda x: x%n != 0, lis)
print(d - len(list(lis)))
