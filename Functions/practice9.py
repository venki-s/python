#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an #eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST

def black_jack(a, b, c):
    
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    else:
        if a == 11 or b == 11 or c ==11:
            return sum((a, b, c)) - 10
        else:
            return 'Bust'
        
print(black_jack(5,6,7))

print(black_jack(9,9,9))

print(black_jack(9,9,11))