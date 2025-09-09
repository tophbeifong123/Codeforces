point_m = 0
point_c = 0
for _ in range(int(input())):
    m,c = [int(x) for x in input().split()]

    if m > c:
        point_m += 1
    elif m < c:
        point_c += 1


if point_m > point_c:
    print("Mishka")
elif point_m < point_c:
    print("Chris")
else:
    print("Friendship is magic!^^")