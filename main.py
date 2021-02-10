import utils
print('Choose from options:\n1. Levenshtein\n2. Soundex')
choice = int(input('Type 1 or 2: '))
if choice == 1:
    word_1 = input('First string: ')
    word_2 = input('Second string: ')
    print(f'Levenshtein distance for "{word_1}" and "{word_2}" is {utils.levenshtein_distance(word_1, word_2)}')
else:
    word = input('Input string: ')
    print(f'Soundex code for "{word}" is {utils.soundex(word)}')
