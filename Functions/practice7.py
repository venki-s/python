#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(mylist):
    
    for index in range(len(mylist)-1):
        if (mylist[index] == 3) and (mylist[index+1] == 3):
            return True
        
        
    return False

print(has_33([1,3,3]))

print(has_33([3,3,3]))

print(has_33([3,3,1]))

print(has_33([3,1,3]))

print(has_33([1,1,1]))

