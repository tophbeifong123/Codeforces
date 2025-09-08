n = list(input())
dp = {
    '2':"abc",
    '3':"def",
    '4':"ghi",  
    '5':"jkl",
    '6':"mno",
    '7':"pqrs",
    '8':"tuv",
    '9':"wxyz"
}
lis = []
w = ""

for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        w += n[i]
    else:
        w += n[i]
        lis.append(w)
        w = ""

w += n[-1]
if w:
    lis.append(w)

for seg in lis:
    digit = seg[0]
    L = len(seg)
    letters = dp[digit]
    k = len(letters)

    q, r = divmod(L, k)
    if r > 0:
        print(letters[r - 1], end="")  
    print(letters[-1] * q, end="")      
