morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    ' ': '/'
}


def regular_morse_code(number):
    if number == "1":
        user_input = input("Type your message you want to translated: ")
        for letter in user_input:
            decording = morse_code[letter.upper()] + ' '
            print(decording, end='')
    elif number == "2":
        user_input = input("Type your message you want to translated: ")
        for letter in user_input:
            decorded = f"{letter}: {morse_code[letter.upper()] + ' '}"
            print(decorded, end='')
    else:
        print("You've entered a higher digit, Please enter a valid input")


let_start = True
while let_start:
    decision = input(
        "Please select the mode for Morse code translation. Type 1 for the regular Morse code format (e.g. "
        "'.-.' for the letter 'R'), or type 2 for the Morse code format that includes the letters you "
        "entered (e.g. '....' for the letter 'H').")
    if decision == "1" or decision == "2":
        regular_morse_code(decision)
        let_start = False
    else:
        print("Please enter a valid input")
