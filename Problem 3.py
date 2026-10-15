#What is the largest prime factor of the number 600851475143?

x = 600851475143
largest_prime = 0

def volgend_priemgetal(x):
    while True:
        x += 1
        test = 2
        is_priem = True
        while test * test <= x:
            if x % test == 0:
                is_priem = False
                break
            test += 1
        if is_priem:
            laatste = x
            return laatste

grootste = 0
vorig = 1
while True:
    priem = int(volgend_priemgetal(vorig))
    vorig = int(volgend_priemgetal(vorig))
    if x % priem == 0:
        x /= priem
        grootste = priem
    if x == 1:
        print(grootste)
        break
