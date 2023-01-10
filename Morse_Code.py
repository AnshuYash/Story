MORSE_CODE_DICT_en = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
                      'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                      'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                      'X': '-..-', 'Y': '-.--', 'Z': '--..', " ": "/", '1': '.----', '2': '..---', '3': '...--',
                      '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                      '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--', '/': '-..-.',
                      '-': '-....-', '(': '-.--.', ')': '-.--.-', ',;': '--..--'}

MORSE_CODE_DICT_de = {'.-': 'A', '-...': "B", '-.-.': 'C', '-..': 'D', '.': 'E',
                      '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K',
                      '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',
                      '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
                      '-..-': 'X', '-.--': 'Y', '--..': 'Z', '/': ' ', '.----': '1', '..---': '2', '...--': '3',
                      '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
                      '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-.-.--': '!', '-..-.': '/',
                      '-....-': '-', '-.--.': '(', '-.--.-': ')'}

key_code = MORSE_CODE_DICT_en.keys()
value_code = MORSE_CODE_DICT_de.keys()
word = ""
word1 = ""


def fun():
    global word
    global word1
    check = input("Enter 'E' for encoding the msg in morse code , or 'D' for decoding the morse code msg.\n").upper()
    if check == "E":
        a1 = (input("Enter your code.\n")).upper()
        for letter in a1:
            for char in key_code:
                if letter == char:
                    word = word + (MORSE_CODE_DICT_en[char]) + " "
        print(word)
        fun()
    elif check == "D":
        a1 = input("Enter your code.\n")
        a2 = a1.split(" / ")
        for char1 in a2:
            a3 = char1.split(" ")
            for char in a3:
                if char in value_code:
                    word1 = word1 + MORSE_CODE_DICT_de[char]
            word1 = word1 + " "
        print(word1)
        fun()
    else:
        res = input("Enter the correct input. Press 'R' to restart coder").upper()
        if res == "R":
            fun()
        else:
            fun()

fun()
