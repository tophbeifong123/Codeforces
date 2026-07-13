for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    even = [x for x in a if x % 2 == 0]
    odd = [x for x in a if x % 2 != 0]

    print(min(len(even), len(odd)))