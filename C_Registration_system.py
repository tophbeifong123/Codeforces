db = {}
for _ in range(int(input())):
    x = input()
    if x not in db:
        print("OK")
        db.update({x:1})
    else:
        print(f'{x}{db[x]}')
        db[x] +=1

