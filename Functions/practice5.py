#MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoga1(str):
    return str[::-1]

def master_yoga2(str):
    
    str1 = ''
    revindex = -1
    
    for index in range(len(str)):
        str1 = str1 + str[revindex]
        revindex = revindex - 1
    
    return str1


def master_yoga3(str):
    
    for index in range(len(str)-1):
       str = str[0:index] + str[-1] + str[index:len(str)-1]

    return str

def master_yoga4(str): 
    return ' '.join(str.split()[::-1])

def master_yoga5(str): 
    reverse_list = str.split(' ')
    final_list = []
    revindex = -1
    
    for index in range(len(reverse_list)):
        final_list.append(reverse_list[revindex])
        revindex = revindex - 1
    
    return ' '.join(final_list)


  



print(master_yoga1('venkat'))

print(master_yoga2('venkat'))

print(master_yoga3('venkat'))

print(master_yoga4('how are you')) 

print(master_yoga5('how are you'))

