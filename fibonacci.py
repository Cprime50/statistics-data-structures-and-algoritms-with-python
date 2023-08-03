#Question (9).
'''    Write a program to sum the first 50 fibonacci sequence.
'''

def fibonacci_sequence():
    fib_sequence = [0, 1]           # starting with the first two numbers (0 and 1).

    while len(fib_sequence) < 50:     # while loop to generate Fibonacci numbers until the length 50 is reached
        next_num = fib_sequence[-1] + fib_sequence[-2]  # Calculating the next Fibonacci number by adding the last two numbers in the sequence

        fib_sequence.append(next_num)        #Add the newly generated fibonacci numb to the end of the sequence using the Append keyword
    
    fib_sum = sum(fib_sequence)
    return fib_sum


result = fibonacci_sequence()
print("The sum of the first 50 Fibonacci numbers are:", result)
