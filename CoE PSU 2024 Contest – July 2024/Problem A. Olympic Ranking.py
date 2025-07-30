lis = []
for _ in range(int(input())):
    G,S,B,T = input().split()
    lis.append((int(G), int(S), int(B), T))

lis.sort(reverse=True, key=lambda x: x[3])
lis.sort(reverse=True, key=lambda x: x[0])

count = 1
for G, S, B, T in lis:
    print(f'{count}: {T} {G} {S} {B} {sum([G, S, B])}')
    count += 1
    