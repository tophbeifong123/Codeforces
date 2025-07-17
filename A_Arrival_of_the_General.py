n = int(input())
lis = list(map(int, input().split()))

max_height = max(lis)
min_height = min(lis)

# หา index ของคนที่สูงที่สุด (ซ้ายสุด)
max_index = lis.index(max_height)

# หา index ของคนที่เตี้ยที่สุด (ขวาสุด)
min_index = n - 1 - lis[::-1].index(min_height)

# คำนวณจำนวน swap
if max_index > min_index:
    count = max_index + (n - 1 - min_index) - 1
else:
    count = max_index + (n - 1 - min_index)

print(count)
