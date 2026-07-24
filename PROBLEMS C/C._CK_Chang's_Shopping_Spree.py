# import sys
# input = sys.stdin.buffer.readline

# n, m = map(int, input().split())
# pr = sorted(map(int, input().split()))

# need = 0
# ans = 0

# for p in pr:
#     # need ใหม่ = ค่าที่มากที่สุดระหว่าง (need เดิม + ราคาจริง p) กับ (10 เท่าของราคา p)
#     need = max(need + p, 10 * p)
#     print(need)

#     if need <= m:
#         ans += 1
#     else:
#         break

# print(ans)


import sys
input = sys.stdin.readline

n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort(reverse=True)

ans = 0

for i in a:
    if i * 10 <= m:
        ans += 1
        m -= i
    else:
        break

print(ans)