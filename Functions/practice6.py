#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there1(n):
    if (90 <= n <= 110) or (190 <= n <= 210):
        return True
    else:
        return False
    
def almost_there2(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
    
print(almost_there1(89))

print(almost_there1(100))

print(almost_there1(111))

print(almost_there1(189))

print(almost_there1(200))

print(almost_there1(211))


print(almost_there2(89))

print(almost_there2(100))

print(almost_there2(111))

print(almost_there2(189))

print(almost_there2(200))

print(almost_there2(211))