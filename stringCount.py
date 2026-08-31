#43 Digits vs Lette4s
def digits_or_letters(s):
    nct = 0
    lct = 0

    for char in s:
        if char.isdigit():
            nct += 1
        elif char.isalpha():
            lct += 1

    print(f"Digits: {nct}, Letters: {lct}")
    if (lct==nct):
       print ("tie")


digits_or_letters("AbC123")  # Output: Digits: 3, Letters: 3
