# lword_ct = 0 lower case words in sentence 
#330

print("Enter sentence to evaluwte:")
S=input('')
s_letters=(len(S))
l_words = []
words = S.split()
word_num = len(words)

print(words)
print("# of chsracters ",s_letters)
print("# of words: ",word_num)


lword_ct = 0
for ct in range(word_num):
    if (words[ct].islower()==True):
       l_words += words[ct]
       lword_ct += 1
      
print(l_words)      


