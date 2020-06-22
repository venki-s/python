#Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(str):
    str_lists = str.split(' ')

    if str_lists[0][0] == str_lists[1][0]:
        return True
    else:
        return False
    

print(animal_crackers('Live Lion'))

print(animal_crackers('Live NLion'))

print(animal_crackers('Live lion'))