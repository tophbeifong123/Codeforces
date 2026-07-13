k1,k2,k3,k4 = [int(x) for x in input().split()]
ans = min(k1,k3,k4) * 256
ans += min(k2,(k1 - min(k1,k3,k4))) * 32
print(ans)