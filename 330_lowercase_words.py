
text = "Hello world this is Python"
words = text.split()

# num of words in a sentence
word_count = len(words)


odd_ct = 0

for index in range (word_count):
   word_len = len(words[index])
   odd = bool(word_len % 2)
   if odd: odd_ct +=1
  
   print("word: ",words[index],"  length: ",word_len," Odd: ",odd)
print("")
print("number of odd wirds i",odd_ct)