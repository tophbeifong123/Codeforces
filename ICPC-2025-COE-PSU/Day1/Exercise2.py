count = 0
try:
    while True:
        n = list(input().split())
        for i in n:
            if "e" in i or "E" in i:
                count += 1
except:
    print(count)