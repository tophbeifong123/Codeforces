n = int(input())
s = [int(x) for x in input().split()]
one = s.count(1)
two = s.count(2)
three = s.count(3)
four = s.count(4)

car = four
four = 0

one_three = min(one, three)
car += one_three
one -= one_three
three -= one_three

car += three
three = 0

car += two // 2
two %= 2   

if two == 1:
    if one >= 2:
        car += 1
        one -= 2
    else:
        car += 1
        one = 0
    two = 0

if one > 0:
    car += (one + 3) // 4
    one = 0

print(car)
