lis = list(input())
lis.sort()

for i in lis:
    if int(i) > 0:
        print(i, end="")