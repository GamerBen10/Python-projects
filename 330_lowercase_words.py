
text = "Hello world this is Python"
words = text.split()

# num of words in a sentence
word_count = len(words)


not_odd_ct = 0

for index in range (word_count):
   word_len = len(words[index])
   not_odd = bool(word_len % 2)
   if not_odd: 
      not_odd_ct +=1
  
   print("word: ",words[index],"  length: ",word_len," Odd: ",not_odd)
print("")
print("number of odd words is",not_odd_ct)