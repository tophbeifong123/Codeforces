def two_pointer(arr,n):
    flag = 1
    left,right = 0,n-1
    while left < right:
        if arr[left] == flag:
            left += 1
            flag += 1
        elif arr[right] == flag:
            right -= 1
            flag += 1
        else:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    p = [int(x) for x in input().split()]
    print(two_pointer(p,n))