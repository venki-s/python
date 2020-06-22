#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    
    total = 0
    
    for rangers in range(2, num):
        isprime = True
        
        for numbers in range(2, rangers):
            if rangers % numbers == 0:
                isprime = False
            
        if isprime or rangers == 2:
            total = total + 1
        
    return total

print(count_primes(100))

print(count_primes(10))

print(count_primes(2))

print(count_primes(1))