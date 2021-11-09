def factorial(n):
    if n <= 0:
        print("Factorial of nonpositive number is not possible")
    else:
        if n == 1:
            return n
        else:
            return n * factorial(n-1)    
    
        
        