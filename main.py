import utils
import checker
from datetime import datetime

if __name__ == '__main__':
    print('Choose from options:\n1. Levenshtein\n2. Soundex\n3.Spell correction')
    choice = int(input('Type 1,2 or 3: '))
    if choice == 1:
        word_1 = input('First string: ')
        word_2 = input('Second string: ')
        print(f'Levenshtein distance for "{word_1}" and "{word_2}" is {utils.levenshtein_distance(word_1, word_2)}')
    elif choice == 2:
        word = input('Input string: ')
        print(f'Soundex code for "{word}" is {utils.soundex(word)}')
    elif choice == 3:
        word = input('Write misspelled word: ')
        a = datetime.now()
        print('Possible options:', *list(checker.spelling_assistant(word)))
