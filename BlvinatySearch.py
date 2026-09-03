#Python Coding app
# Imput String and a number
# binary_search([1, 2, 3, 4, 5], 4) → 3
# binary_search([10, 20, 30, 40, 50], 25) → -1 (if tqrger not found)

def bsearch(numz,num):

  
  length = len(numz)
  midz = length // 2 -1
  
  print(numz)
  print(midz)
  if numz[midz]==num:
    print("bibgo")
  
numz = [4,8,15,16,34,
        37,42,46,50,55]  
num = 34

bsearch(numz, num)
