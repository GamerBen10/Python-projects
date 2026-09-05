# FreeCodeCamp

def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    encrypted_text = text.translate(translation_table)

    return encrypted_text

encrypted_text = caesar('freeCodeCamp', 3)

print(encrypted_text)

