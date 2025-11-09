for _ in range(int(input())):
    arr = ''
    for _ in range(8):
        s = list(input())
        for i in s:
            if i.isalpha():
                arr += i
    print(arr)
    arr = ''