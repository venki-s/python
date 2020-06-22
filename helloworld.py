def myfunc(str):
    mystr = ''
    counter = 0;
    for item in str:
        if counter%2 == 0:
            mystr = mystr + item.upper()
        else:
            mystr = mystr + item.lower()
        counter = counter + 1
    
    return mystr

str1 = myfunc('hElLo')
print(str1)