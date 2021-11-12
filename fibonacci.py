
def fibonacci_digit(index):
    if index <= 1:
        return 1
    else:
        return (fibonacci_digit(index - 1) + fibonacci_digit(index - 2)) # returns (n+1)th digit of the fibonacci sequence
    
def fibonacci_list(first_x):
    fib_list = [1,1]
    counter = 2 # index will be one less
    while first_x > counter:
        fib_list.append(fib_list[counter - 1] + fib_list[counter - 2]) # takes the last value of list, so no need to add 1 to counter
        counter += 1
    return fib_list[0:first_x]  # exclusive terminal value, no need to add one  
        
    
    