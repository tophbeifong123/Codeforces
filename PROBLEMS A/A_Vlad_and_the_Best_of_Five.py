for _ in range(int(input())):
    arr = list(input())
    count_A = arr.count('A')
    count_B = arr.count('B')

    if count_A > count_B:print('A')
    else:print('B')