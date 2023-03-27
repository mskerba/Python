import sys

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
    ' ' : '/'
}


def morse_transform(string):
    str = ""
    for item in string:
        if item.islower():
            item = item.upper()
        str +=  morse_code[item] + " "
    print (str)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit(0)
    for i in range(2, len(sys.argv)):
        sys.argv[1] += ' ' + sys.argv[i]
    for item in sys.argv[1]:
        if item.isdigit() == 0 and item.isalpha() == 0 and item != ' ':
            print("ERROR")
            exit(0)
    morse_transform(sys.argv[1])
