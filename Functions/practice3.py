#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(a, b):

    if a == 20 or b == 20 or a+b == 20:
        return True
    else:
        return False


print(makes_twenty(20, 1))
#True

print(makes_twenty(-2, 20))
#True

print(makes_twenty(2, 18))
#True

print(makes_twenty(-2, 22))
#True

print(makes_twenty(2, 4))
#False