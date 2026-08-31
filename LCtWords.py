
#330
def get_lowercase_words(S):

   s_letters=(len(S))
   l_words = []
   words = S.split()
   word_num = len(words)
   lword_ct = 0 

 #  print(words)
 #  print("# of chsracters ",s_letters)
 #  print("# of words: ",word_num)


   lword_ct = 0
   for ct in range(word_num):
      if (words[ct].islower()==True):
         l_words.append(words[ct])
         lword_ct += 1
   print(l_words)
   print(type(l_words))
   return(l_words)   

get_lowercase_words("hello GOOD world")


