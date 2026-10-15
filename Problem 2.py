x = 1
y = 2
antwoord = 0
fibonacci = 0

while True:
    fibonacci = x + y
    if fibonacci > 4000000:
        break 
    if fibonacci % 2 == 0:
        antwoord += fibonacci
    x = y
    y = fibonacci
    print(x, y, fibonacci)
    
print(antwoord)