import math

x = 0
antwoord = 0

while x < 162000:
    y = x**2
    if y % 2 != 0:
        antwoord += y
    x += 1
print(antwoord)