#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(a, b):

    if a == 20:
        return True
    elif b == 20:
        return True
    elif a+b == 20:
        return True
    else:
        return False


print(makes_twenty(20, 1))

print(makes_twenty(-2, 20))

print(makes_twenty(2, 18))

print(makes_twenty(-2, 22))

print(makes_twenty(2, 4))