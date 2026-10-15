# Which starting number, under one million, produces the longest chain? (Collatz sequence)

original_number = 2
longest_chain = 0
number_longest_chain = 0

while original_number < 1000000:
    steps = 0
    
    n = original_number
    while n != 1:
        if n % 2 == 0:
            n /= 2
            steps += 1
        else:
            n = 3*n + 1
            steps += 1
    
    if steps > longest_chain:
        longest_chain = steps
        number_longest_chain = original_number
    
    original_number += 1
print(number_longest_chain, longest_chain)