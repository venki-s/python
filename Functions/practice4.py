# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name


def old_mcdonald(str):
    
    if len(str) > 3:
        return str[0].upper() + str[1:3] + str[3].upper() + str[4:]
    elif len(str)>0 and len(str)< 4:
        return str[0].upper() + str[1:]
    else:
        return str

print(old_mcdonald('ven'))
# Venp

print(old_mcdonald('venkat'))
# VenKat

print(old_mcdonald('ven at'))
# Ven at

print(old_mcdonald(' '))
# 
