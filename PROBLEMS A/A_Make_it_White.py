for _ in range(int(input())):
    n = int(input())
    s = list(input())
    Black_index = [i for i,item in enumerate(s) if item == 'B']
    print(1) if len(Black_index) == 1 else print(Black_index[-1] - Black_index[0] + 1)