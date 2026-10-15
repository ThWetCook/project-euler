x = 1
y = 1
antwoord_x = 0
antwoord_y = 0

while x <= 333:
    a = x * 3
    if a % 5 != 0:
        antwoord_x += a
    x+= 1
    
while y < 200:
    b = y * 5
    antwoord_y += b
    y += 1

antwoord = antwoord_x + antwoord_y
print(antwoord)
