#Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
#lesser_of_two_evens

def lesser_even(a, b):

    if  a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_even(2,4))
#2

print(lesser_even(1,4))
#4

print(lesser_even(3,9))
#9

print(lesser_even(0,4))
#0

print(lesser_even(0,0))
#0

print(lesser_even(0, -1))
#0

print(lesser_even(-9, -1))
#-1

print(lesser_even(-2, -4))
#-4
