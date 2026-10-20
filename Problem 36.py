number = 0
sum = 0
while number < 1000000:
    number_bin = str(bin(number)).replace("0b", "")
    
    if number_bin[::-1] == number_bin and str(number)[::-1] == str(number):
        sum += number
    number += 1
print(sum)