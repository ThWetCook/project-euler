# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


number = 0
totaal = 0
som_getal = 0

while number < 10000000:
    som_getal = 0
    for i in str(number):
        som_getal += int(i)**5
    if som_getal == number:
        totaal += som_getal
    number += 1
print(totaal-1)
