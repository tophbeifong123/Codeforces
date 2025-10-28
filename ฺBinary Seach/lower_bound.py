def lower_bound(arr, target):
    left,right = 0 , len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left

print(lower_bound([1,2,3,4,5,6,7,8,9],5))  # Output: 4