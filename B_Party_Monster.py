for _ in range(int(input())):
    n = int(input())
    s = list(input())
    cl = s.count('(')
    cr = s.count(')')

    print('YES') if cl == cr else print('NO')