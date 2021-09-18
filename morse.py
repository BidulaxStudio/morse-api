code = {

    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",

    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    "\"": ".-..-.",
    "?": "..--..",
    "/": "-..-."

}


def text_to_morse(text):

    """
    :param text: Text to convert
    :return: Morse converted
    """

    text = text.upper()
    morse = ""
    iter = 0

    for char in text:

        iter += 1

        if char == " ":
            morse += "   "

        else:

            if char not in code:
                return f"% UNABLE TO FIND CHAR '{char}'"

            morse += code[char]

            if iter != len(text) and text[iter] != " ":
                morse += " "

    return morse


def morse_to_text(morse):

    """
    :param morse: Morse to convert
    :return: Text converted
    """

    done = 0
    text = ""

    words = morse.split("   ")

    for word in words:

        chars = word.split(" ")

        for char in chars:

            found = False

            for key, value in code.items():
                if char == value:
                    text += key
                    found = True

            if not found:
                return f"% UNABLE TO FIND CHAR '{char}'"

        done += 1

        if done != len(words):
            text += " "

    return text
