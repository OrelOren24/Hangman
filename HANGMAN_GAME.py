
MAX_TRIES = 7
num_of_tries = 1
HANGMAN_ASCII_ART = """
 _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/
                         """
print(HANGMAN_ASCII_ART, MAX_TRIES)


def print_hangman(num_of_tries):
    """
Display the seven modes of hangman.
param1 = num_of_tries
type param1 = dict
return = 7 modes with numbers of tries.
rtype = dict
    """
    HANGMAN_PHOTOS = {
        1: """
x------x""",
        2: """
x------x
|
|
|
|
|""",
        3: """
x-------x
|       |
|       0
|
|
|""",
        4: """
x-------x
|       |
|       0
|       |
|
|""",
        5: """
x------x
|      |
|      0
|     /|\\
|
|""",
        6: """
x------x
|      |
|      0
|     /|\\
|     /
|""",
        7: """
x------x
|      |
|      0
|     /|\\
|     / \\
|"""}
    return HANGMAN_PHOTOS[num_of_tries]


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Display the Conditions of hangman game
    param1 : letter_guessed
    param2 : old_letter_guessed
    type: string
    return: The Correctness in the word
    rtype: string
    """
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed) is False:
        print('X\n' + ' --> '.join(old_letters_guessed) + '\nFalse-', 'The letter is not valid')
        return False
    old_letters_guessed.append(letter_guessed)
    print('The letter is valid')
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """
    Show the word to guess and the letters in old_letters_guessed
    param1 = secret_word
    param2 = old_letters_guessed
    type param1 = str
    type param2 = list
    return = Results of the guess
    rtype = str
    """
    new_str = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            new_str += letter
        else:
            new_str += '_'
    return ' '.join(new_str)


def check_win(secret_word, old_letters_guessed):
    """
    Display True/False if thw whole word guesses successfully.
    param1 = secret_word
    param2 = old_letters_guessed
    type param1 = str
    type param2 = list
    return = Bool condition
    rtype = str
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False

    return True


# מדובר בפונקציה הזאת, שצריך שהמספר אינדקס שאבחר בקובץ(המילה) תהיה המילה של הניחוש
def choose_word(file_path: str, index: int) ->tuple:
  with open(file_path, 'r') as f:
    words = f.read().split()
  return len(set(words)), words[ (index + 1) % len(words)]


def main():
    global num_of_tries
    old_letters_guessed = []
    print('WELCOME TO HANGMAN GAME')
    print(print_hangman(1))
    file_path = input("insert path: ").replace('\\', '\\\\')
    index = int(input("enter a number: "))
    secret_word = choose_word(file_path,index)
    print(secret_word)
    while True:
        letter_guessed = input('Guess a letter: ')
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            print(old_letters_guessed)
            print(show_hidden_word(secret_word, old_letters_guessed))
            if letter_guessed not in secret_word and num_of_tries < MAX_TRIES:
                num_of_tries += 1
                print(print_hangman(num_of_tries))
                if print_hangman(num_of_tries) != print_hangman(7):
                    print('Try again :(')
        if check_win(secret_word, old_letters_guessed):
            print("YOU WIN")
            break
        elif num_of_tries >= MAX_TRIES:
            print("YOU LOST")
            break


if __name__ == '__main__':
    main()
