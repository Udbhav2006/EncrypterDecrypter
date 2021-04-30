import string

d = {
    "a": "6766",
    "b": "732",
    "c": "2679",
    "d": "648",
    "e": "68642",
    "f": "450",
    "g": "12388",
    "h": "398",
    "i": "08890",
    "j": "193",
    "k": "389",
    "l": "235",
    "m": "7109",
    "n": "26538",
    "o": "6386",
    "p": "2943",
    "q": "5754",
    "r": "53454",
    "s": "984",
    "t": "5064",
    "u": "33450",
    "v": "12563",
    "w": "0713",
    "x": "291",
    "y": "457",
    "z": "0351",
    "1": "2912",
    "2": "592",
    "3": "828",
    "4": "1038",
    "5": "01010",
    "6": "7193",
    "7": "2019",
    "8": "1923",
    "9": "012",
    "0": "0296",
    "!": "941",
    "@": "019",
    "#": "5102",
    "$": "731",
    "%": "1199",
    "^": "5885",
    "&": "911",
    "*": "100",
    "(": "482",
    ")": "191",
    "-": "0011",
    "_": "777",
    "=": "4059",
    "+": "783",
    "[": "438",
    "{": "111",
    "]": "333",
    "}": "3322",
    "\\": "185",
    "|": "010",
    ";": "555",
    ":": "888",
    "'": "999",
    '"': "333",
    ",": "666",
    "<": "222",
    ">": "1001",
    ".": "465",
    "/": "777",
    "?": "234",
    "`": "932",
    "~": "526"
}


def encrypt(text):
    words = text.split(' ')
    letters = []
    encrypted_letters = []
    for word in words:
        for letter in word:

            letters.append(letter)
        letters.append('§')

    for letter in letters:
        if letter == '§':
            encrypted_letters.append('§')

        if letter in string.ascii_uppercase:
            letter1 = d[letter.lower()]
            encrypted_letters.append(letter1)
            encrypted_letters.append('↔')
            encrypted_letters.append('∞')

        elif letter in string.printable:
            letter1 = d[letter]
            encrypted_letters.append(letter1)

            encrypted_letters.append('∞')

    encrypted_letters.pop()
    text2 = ''.join(encrypted_letters)
    encrypted_text = text2[::-1]
    print('Here is your encrypted text: ')
    print(encrypted_text)


def decrypt(text):
    text = text[::-1]

    words = text.split('§')
    decrypted_text = ''
    key_list = list(d.keys())
    vals_list = list(d.values())
    for word in words:
        letters = word.split('∞')
        letters.pop()
        for letter in letters:
            cap = False
            if '↔' in letter:
                letter = letter.strip('↔')
                cap = True
            key = key_list[vals_list.index(letter)]
            if cap:
                key = key.upper()
            decrypted_text += key
        decrypted_text += ' '
    print('Here is your decrypted text: ')
    print(decrypted_text)

run = True
while run:
    text = input('Enter your text: ')
    todo = 'jfsodijfsdfod'
    while todo.lower() not in ['e', 'd']:
        todo = input('Do you want to encrypt[e] or decrypt[d]: ')
    if todo == 'e':
        encrypt(text)
    elif todo == 'd':
        decrypt(text)

    choice = 'asd'
    while choice not in['q', 'c']:
        choice = input('Do you want to quit[q] or continue[c]? ')

    if choice == 'c':
        continue
    else:
        break
