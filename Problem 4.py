#txt = "Hello World"[::-1]

x = 100
y = 100
grootste = 0

while True:
    a = str(x * y)
    if a == a[::-1]:
        if int(a) > int(grootste):
            grootste = a
        
    if x == 999:
        x = 100
        y += 1
    else:
        x += 1
    
    if x == 999 and y == 999:
        break
print(grootste)