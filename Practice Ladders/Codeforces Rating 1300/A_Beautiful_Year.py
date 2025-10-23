# n = input()

# while True:
#     n = str(int(n) + 1)
#     if n[0] != n[1] and n[0] != n[2] and n[0] != n[3] and n[1] != n[2] and n[1] != n[3] and n[2] != n[3]:
#         print(n)
#         break

n = int(input())

while True:
    n += 1
    s = str(n)
    if len(set(s)) == 4:
        print(n)
        break