message = '  Hello, Python World!  '

print(message.strip())
print(message.strip().lower())
print(message.strip().replace('Python', 'Coding'))

words = 'red,green,blue'.split(',')
print(words)
print('-'.join(words))

text = 'Programming'
print(text[0], text[-1], text[0:4]) 