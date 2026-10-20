array = []

a = 2
b = 2

while a <= 5 and b <= 5:
    if a != 5:
        x = a**b
        print(x)
        a += 1
    if a == 5:
        x = a**b
        print(x)
        b += 1