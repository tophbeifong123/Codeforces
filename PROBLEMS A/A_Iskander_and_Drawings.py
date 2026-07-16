# for _ in range(int(input())):
#     n = int(input())
#     s = list(input())
#     point = 0
#     m = 0

#     for i in range(n):
#         if s[i] == '#':
#             point += 1
#             m = max(m,point)
#         else:
#             point = 0

#     print((m + 2 - 1) // 2)


for _ in range(int(input())):
    n = int(input())
    s = input().split('*')
    ans = (len(max(s)) + 2 -1) // 2
    print(ans) 