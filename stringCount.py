def digits_or_letters(s):

   nct = 0
   lct = 0
   ln = len(s)
   print(ln)
  
   for x in range(ln):
      print(x)
      if s.isdigit():  # True
         nct+=1
   else:
      if s.isalpha(): # True
         lct+=1
   print (nct, lct)
   return s

digits_or_letters("AbC123")

