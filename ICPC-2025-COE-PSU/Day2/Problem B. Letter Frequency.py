db = {}
try:
    a = list(input())
    while True:
        for i in a:
            if i.isalpha() == True:
                if i.upper() in db:
                    db[i.upper()] += 1
                else:
                    db[i.upper()] = 1
        a = list(input())
except:
    for i in sorted(db,key=lambda x:db[x],reverse=True):
        print(db[i],i)