alphalist = []
shift = 5


# Populate the list using .append()
for i in range(ord('A'), ord('Z') + 1):
    alphalist.append(chr(i))
print(alphalist)
print(" ")

# Cesar Cypher
# Slice from index 5 to end, then append the first 5 characters
shiftedalpha= alphalist[5:] + alphalist[:5]

print(shiftedalpha)
print(" ")

lower_chars=("abc")
upper_chars=("ABC")

table_str = (lower_chars,upper_chars)
print(table_str)


"""
mapping = {"a": "4", "e": "3", "o": "0"}
table = str.maketrans(mapping)
print("hello all".translate(table)) # Output: 'h3ll0 4ll'
"""







