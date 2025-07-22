for _ in range(int(input())):
    s = input()
    if "FFT" in s or "NTT" in s:
        s = sorted(s, reverse=True) 
        print(''.join(s))
    else:
        print(s)
