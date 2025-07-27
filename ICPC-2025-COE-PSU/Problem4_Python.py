x = [int(x) for x in list(input())]
x.sort(reverse=True)
for i in x:
    print(i, end="")