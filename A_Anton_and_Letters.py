lis = input()
x = lis.replace("{","")
x = x.replace("}","")
x = x.replace(",","")
y = x.split()
print(len(set(y)))