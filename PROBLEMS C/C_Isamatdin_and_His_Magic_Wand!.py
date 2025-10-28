for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    has_odd = any(x % 2 != 0 for x in arr)
    has_even = any(x % 2 == 0 for x in arr)
    if has_odd and has_even:
        print(*sorted(arr))
    else:
        print(*arr)