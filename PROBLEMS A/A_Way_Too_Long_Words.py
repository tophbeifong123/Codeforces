for _ in range(int(input())):
    s = list(input())
    if len(s) > 10:
        print(f'{s[0]}{len(s) - 2}{s[-1]}')
    else:
        print(''.join(s))