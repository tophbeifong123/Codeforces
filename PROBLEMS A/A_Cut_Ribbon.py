n, a, b, c = map(int, input().split())

# สร้าง dp ที่ index i หมายถึง ความยาว i ของริบบิ้น
dp = [-1] * (n + 1)
dp[0] = 0  # ความยาว 0 ตัดได้ 0 ชิ้น

for i in range(1, n + 1):
    for length in [a, b, c]:
        if i >= length and dp[i - length] != -1:
            dp[i] = max(dp[i], dp[i - length] + 1)

print(dp[n])
