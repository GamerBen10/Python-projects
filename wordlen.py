words = ["i","am","the","best","you","are","the","worst","ever"]


listlen = len(words)
print(listlen)
listct = 0
newlist = []
x = 0
words = ["i", "am", "the", "best", "you", "are", "the", "worst", "ever"]
listlen = len(words)

for x, word in enumerate(words):
    wordlen = len(word)
    print(x, listlen, wordlen, word)

    
"""
    if wordlen > 5:
       print(x, wordlen,words[x])
    newlist.append(words[listct])
    listct += 1
 
   
   if (words[index]) > (wordlen):
    #print(words[index])
print(newlist)