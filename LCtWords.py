
def get_lowercase_words(S):
    l_words = []
    for word in S.split():
        if word.islower():
            l_words.append(word)
    return " ".join(l_words)


print(get_lowercase_words("hello GOOD world"))
print(get_lowercase_words("these are all lowercase"))
print(get_lowercase_words("less is NoT more"))
print(get_lowercase_words("DonT eat pizza every OTHER day"))
print(get_lowercase_words("Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog"))
