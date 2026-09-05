def decode_morse(code):
    encoded_words = []

    # Split input by words
    for wordz in code.split():
        encoded_letters = []

        for letterz in wordz:
            match letterz.upper():
                case "A":
                    morse = ".-"
                case "B":
                    morse = "-..."
                case "C":
                    morse = "-.-."
                case "D":
                    morse = "-.."
                case "E":
                    morse = "."
                case "F":
                    morse = "..-."
                case "G":
                    morse = "--."
                case "H":
                    morse = "...."
                case "I":
                    morse = ".."
                case "J":
                    morse = ".---"
                case "K":
                    morse = "-.-"
                case "L":
                    morse = ".-.."
                case "M":
                    morse = "--"
                case "N":
                    morse = "-."
                case "O":
                    morse = "---"
                case "P":
                    morse = ".--."
                case "Q":
                    morse = "--.-"
                case "R":
                    morse = ".-."
                case "S":
                    morse = "..."
                case "T":
                    morse = "-"
                case "U":
                    morse = "..-"
                case "V":
                    morse = "...-"
                case "W":
                    morse = ".--"
                case "X":
                    morse = "-..-"
                case "Y":
                    morse = "-.--"
                case "Z":
                    morse = "--.."
                case _:
                    morse = "?"

            encoded_letters.append(morse)

        # Join letters in a word with a space
        encoded_words.append(" ".join(encoded_letters))

    # Join distinct words with a forward slash
    return " / ".join(encoded_words)


result = decode_morse("sos")
print(result)