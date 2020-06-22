#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order


def spy_game1(mylist):
    
    for findex in range(len(mylist)):
        if mylist[findex] == 0:
            for sindex in range(findex+1, len(mylist)):
                if mylist[sindex] == 0:
                    for tindex in range(sindex+1, len(mylist)):
                        if mylist[tindex] == 7:
                            return True
        
    return False

def spy_game2(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   
       
    return len(code) == 1
 
print(spy_game1([1,2,4,0,0,7,5]))   
 
print(spy_game1([1,0,2,4,0,5,7])) 
  
print(spy_game1([1,7,2,0,4,5,0])) 


print(spy_game2([1,2,4,0,0,7,5]))   
 
print(spy_game2([1,0,2,4,0,5,7])) 
  
print(spy_game2([1,7,2,0,4,5,0])) 