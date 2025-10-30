for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    result = [x for x in a if x == max(a)]
    print(sum(result) // len(result))