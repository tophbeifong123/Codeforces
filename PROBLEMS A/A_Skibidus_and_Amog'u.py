for _ in range(int(input())):
    w = list(input())
    w[-2::] = 'i'
    print(''.join(w))