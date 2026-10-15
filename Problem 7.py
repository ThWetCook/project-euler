aantal_priem = 0
x = 1
laatste = 0

while aantal_priem < 10001:
    x += 1
    test = 2
    is_priem = True
    while test * test <= x:
        if x % test == 0:
            is_priem = False
            break
        test += 1
    if is_priem:
        aantal_priem += 1
        laatste = x

print(aantal_priem, laatste)