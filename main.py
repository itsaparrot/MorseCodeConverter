letters_dict = {' ': '/', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
                'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
                'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}


# translates user input letters to morse code
def letters_to_morse():
    user_words = input('Type words to be translated to morse: ').lower()
    translated_word = []
    valid_characters = True
    for character in user_words:
        if character in letters_dict:
            translated_word.append(letters_dict[character])
        else:
            valid_characters = False
    if valid_characters:
        print(' '.join(translated_word))
    else:
        print('Invalid characters. Valid characters include a-z, and 0-9.')


# translates user input morse code to letters
def morse_to_letters():
    user_morse = input('Type the morse code using "." and "-" symbols: ').lower()
    user_morse_list = user_morse.split()
    translated_morse = []
    valid_morse = True
    # inverts dictionary key value pairs, keys will be now morse code, values will be letters
    morse_dict = {morse: letter for letter, morse in letters_dict.items()}
    for character in user_morse_list:
        if character in morse_dict:
            translated_morse.append(morse_dict[character])
        # morse code may have '/' for readability, this will skip those cases
        elif character == '/':
            pass
        else:
            valid_morse = False
    if valid_morse:
        print(''.join(translated_morse))
    else:
        print('Invalid morse characters.')

# main loop, continues until user declines to continue
user_response = True
while user_response:
    valid_response = True
    while valid_response:
        answer = input('Type "text" if you want to translate text to morse, or type "morse" if you want to translate '
                       'morse to text: ').lower()
        if answer == 'text':
            letters_to_morse()
        elif answer == 'morse':
            morse_to_letters()
        valid_response = False

    continue_question = input('Would you like to keep translating? "y" or "n" ')
    if continue_question == 'n':
        user_response = False

