import math 

for _ in range(int(input())):
    N,M,K,r1,c1,r2,c2 = [int(x) for x in input().split()]
    r1,c1,r2,c2 = math.ceil(r1 / K),math.ceil(c1 / K),math.ceil(r2 / K),math.ceil(c2 / K)

    print(r1,c1,r2,c2)
    print((abs(r1 - r2) + 1 ) * (abs(c1- c2) + 1))