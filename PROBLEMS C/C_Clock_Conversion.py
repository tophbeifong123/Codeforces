for _ in range(int(input())):
    s = input().split(':')
    if int(s[0]) <= 12:
        if s[0] == '12' and s[1] == '00':
            print('12:00 PB')
        print(f'{s[0]}:{s[1]} AM')
    else:
        print(f'0{int(s[0]) - 12}:{s[1]} PM')