
#330
def get_lowercase_words(S):
    l_words = []
    for word in S.split():
        if word.islower():
            l_words.append(word)
          
    return " ".join(l_words)


print(get_lowercase_words("hello GOOD world"))
"""
get_lowercase_words("these are all lowercase")
get_lowercase_words("less is NoT more")
get_lowercase_words("DonT eat pizza every OTHER day")
get_lowercase_words("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog")

get_lowercase_words("hello GOOD world")
"""

