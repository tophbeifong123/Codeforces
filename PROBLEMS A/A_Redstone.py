from itertools import combinations

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    comb = combinations(a,2)
    result = [pair for pair in comb if pair[0] == pair[1]]

    if len(result) > 0:
        print("YES")
    else:
        print("NO")

# case 2
# for _ in range(int(input())):
#     n = int(input())
#     a = [int(x) for x in input().split()]

#     if len(set(a)) < n:
#         print("YES")
#     else:
#         print("NO")

# case 1
# for _ in range(int(input())):
#     n = int(input())
#     a = [int(x) for x in input().split()]
#     flag = False

#     for i in range(n):
#         for j in range(i+1,n):
#             if a[i] == a[j]:
#                 flag = True
    
#     if flag :
#         print("YES")
#     else:
#         print("NO")