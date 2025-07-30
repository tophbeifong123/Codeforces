n = list(input())
result = ""
i = 0 

while i < len(n):
    if n[i] == ".":
        result += "0"
        i += 1
    elif n[i] == "-":
        if n[i+1] == ".":
            result += "1"
        else:
            result += "2"
        i += 2
print(result)