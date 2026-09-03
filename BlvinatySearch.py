#Python Coding app
# Imput String and a number
# binary_search([1, 2, 3, 4, 5], 4) → 3
# binary_search([10, 20, 30, 40, 50], 25) → -1 (if tqrger not found)

def bsearch(numz,num):

  
  length = len(numz)
  midz = length // 2
  print(numz, length, midz)
  print(numz[midz])
  
  
numz = [4,8,15,16,37,
        34,42,46,50,55]  
num = 7

bsearch(numz, num)
