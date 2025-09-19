n = int(input())

if n < 0:
    n = list(str(abs(n)))
    n.remove(n.index(max(n)))
else:
    print(n)