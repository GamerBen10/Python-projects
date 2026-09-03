text = "Hello world this is Python"
words = text.split()

# num of words in a sentence
word_count = len(words)


for index in range (word_count):
   word_len = len(words[index]) 
   print("word: ",words[index],"  length: ",word_len,"  ",word_len % 2)  
  
