def vol(r):
    return (4.0/3.0)*(22.0/7.0)*r*r*r

def ran_check(num, low, high):
    return low <= num <= high

def up_low(s):
    num_low = 0
    num_up = 0
    
    for item in s:
        if item.islower():
            num_low = num_low + 1
        else:
            num_up = num_up +1
            
    return num_low, num_up

def unique(mylist):
    
    final_list = []
    
    for item in mylist:
        if not item in final_list:
            final_list.append(item)
            
    return final_list

def multiply(mylist):
    
    total = 1
    
    for item in mylist:
        total = total * item
        
    return total

def palindrome(str):
    
    if str == str[::-1]:
        return True
    else:
        return False
    
def ispanagram(str):
    
    alpha = ['a' , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for item in str:
        if item in alpha:
            alpha.remove(item)
    
    return len(alpha) == 0

print(vol(2))

print(ran_check(2, 1, 5))

print(ran_check(2, 4, 9))

print(up_low('Hello How Are You'))

print(unique([1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 6]))

print(multiply([1,2,3,4]))

print(palindrome('heeh'))

print(palindrome('now'))

print(ispanagram('abcd efghijklmnop qrstuvwxyz'))

print(ispanagram('The quick brown fox jumps over the lazy dog'))