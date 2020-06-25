#Create a generator that generates the squares of numbers up to some number N.

def gensquares(n):
    for num in range(n):
        yield num ** 2

for x in gensquares(10):
    print(x)

print('\n')
#Create a generator that yields "n" random numbers between a low and high number (that are inputs).

import random

def random_num(low, high, n):
    for num in range(n):
        yield random.randint(1,10)
    
for num in random_num(1,10,12):
    print(num)


print('\n')
#Use the iter() function to convert the string below into an iterator:

s = 'hello'
s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))