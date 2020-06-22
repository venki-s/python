#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(str):
    
    final_str = ''
    for item in str:
        final_str = final_str + 3*item
  
    return final_str
        
print(paper_doll('hello'))

