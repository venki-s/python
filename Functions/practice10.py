def summer_69(mylist):
    
    total = 0
    
    for item in mylist:
        if item<6 or item>9:
            total = total + item
            
    return total

print(summer_69([1, 3, 5]))

print(summer_69([4, 5, 6, 7, 8, 9]))

print(summer_69([2, 1, 6, 9, 11]))
