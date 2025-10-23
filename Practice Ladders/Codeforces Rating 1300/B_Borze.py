# Borze = list(input())
# result = []
# flag = ''

# for i in Borze:
#     flag += i 
#     if flag == '.':
#         result.append('0')
#         flag = ''
#     elif flag == '-.':
#         result.append('1')
#         flag = ''
#     elif flag == '--':
#         result.append('2')
#         flag = ''
    
# print(*result, sep='')

Borze = input()
i = 0
result = ''

while i < len(Borze):
    if Borze[i] == '.':
        result += '0'
        i += 1
    else:
        if Borze[i+1] == '.':
            result += '1'
        else:
            result += '2'
        i += 2

print(result)