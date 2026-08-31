
#330
def get_lowercase_words(S)

s_letters=(len(S))
l_words = []
words = S.split()
word_num = len(words)
lword_ct = 0 

print(words)
print("# of chsracters ",s_letters)
print("# of words: ",word_num)


lword_ct = 0
for ct in range(word_num):
    if (words[ct].islower()==True):
       l_words.append(words[ct])
       lword_ct += 1
      
return(l_words)   

instring=("hello GOOD world")
answer=(get_lowercase_words(instring)

print(answer)