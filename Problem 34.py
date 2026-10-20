import math

number = 0
totaal = 0
som_getal = 0

while number < 10000000:
    som_getal = 0
    for i in str(number):
        som_getal += math.factorial(int(i))
    if som_getal == number:
        totaal += som_getal
    number += 1
print(totaal-2-1)
