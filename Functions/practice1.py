#Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
#lesser_of_two_evens

def lesser_even(a, b):

    alleven = True
    if not a%2 == 0:
        alleven = False
    if not b%2 == 0:
        alleven = False

    if alleven:
        return min(a,b)
    else:
        return max(a,b)


lesser = lesserEven(2,4)
print(lesser)
#2

lesser = lesserEven(1,4)
print(lesser)
#4

lesser = lesserEven(3,9)
print(lesser)
#9

lesser = lesserEven(0,4)
print(lesser)
#0

lesser = lesserEven(0,0)
print(lesser)
#0

lesser = lesserEven(0, -1)
print(lesser)
#0

lesser = lesserEven(-9, -1)
print(lesser)
#-1

lesser = lesserEven(-2, -4)
print(lesser)
#-4
