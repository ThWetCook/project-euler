# Find the sum of all the primes below two million.

def is_priem(x):
    test = 2
    is_priem = True
    while test * test <= x:
        if x % test == 0:
            is_priem = False
            break
        test += 1
    if is_priem:
        return True
    else:
        return False

antwoord = 0
x = 1
while x < 2000000:
    priem = is_priem(x)
    if priem == True:
        antwoord += x
    x +=1
antwoord -= 1 # 1 is geen priemgetal, maar dit programma telt hem wel mee
print(antwoord)