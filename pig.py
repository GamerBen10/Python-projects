import random

def roll():
    min_value = 1
    max_value = 6
    totalct = 0
    continued = True
    
    while continued == True:
    # Roll a random number between 1 and 6
        rolled = random.randint(min_value, max_value)
        print(rolled)
        totalct += rolled
        
        if rolled == min_value:
         continued = False
         
    return totalct-1

print(roll())
