# k = int(input())
# f = 1
# ans = 0

# for i in range(1,k):
#     f = (f * 2) + 1
#     ans += 1
#     if f >=  k:
#         break

# print(ans)
import math
k = int(input())

print(int(math.log10(k)//math.log10(2)))