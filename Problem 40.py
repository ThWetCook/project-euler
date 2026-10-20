x = 1
number = "0."

while True:
    number = str(str(number) + str(x))
    x += 1
    if len(number) > 1000001:
        break

index = -1
total = 1
for i in number:
    if index == 1:
        total *= int(i)
        print(i)
    elif index == 10:
        total *= int(i)
        print(i)
    elif index == 100:
        total *= int(i)
        print(i)
    elif index == 1000:
        total *= int(i)
        print(i)
    elif index == 10000:
        total *= int(i)
        print(i)
    elif index == 100000:
        total *= int(i)
        print(i)
    elif index == 1000000:
        total *= int(i)
        print(i)
    index += 1
print(total)
