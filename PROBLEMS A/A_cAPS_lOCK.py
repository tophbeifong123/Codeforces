n = input()
x = list(n)

if n[1::].isupper() or len(n) == 1 :
    for i in x:
        if i.isupper() :
            print(i.lower(),end='')
        else:
            print(i.upper(),end='')
else:
    print(n)