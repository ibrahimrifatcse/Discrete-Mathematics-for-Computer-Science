def fib(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Handling negative n
    if n < 0 and n % 2 == 0:
        return fib(-n)
        
    if n < 0 and n % 2 != 0:
        return -fib(-n)
        
    # Recursive case
    return fib(n - 1) + fib(n - 2)

# Test cases
print(fib(-4))
