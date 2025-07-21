# lis = [5,8,7,1,9,4,1,2,6]
# m = lis[0]
# for i in range(len(lis)):
#     if m > lis[i]:
#         m = lis[i]

# print(m)

lis = [5,8,7,1,9,4,1,2,6]

for i in range(len(lis)- 1):
    if lis[i] > lis[i+1]:
        lis[i], lis[i+1] = lis[i+1], lis[i]

print(lis)