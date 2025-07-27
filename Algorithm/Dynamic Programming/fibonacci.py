cache = {}

def fib(a):
    if a <= 0:
        return 0
    elif a == 1:
        return 1
    if a in cache:
        return cache[a]
    else:
        cache[a] = fib(a - 1) + fib(a - 2)
        return cache[a]
    
print(fib(int(input())))