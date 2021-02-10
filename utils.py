import re

def levenshtein_distance(first_word, second_word):
    length_first_word = len(first_word)
    length_second_word = len(second_word)
    if length_first_word > length_second_word:
        first_word, second_word = second_word, first_word
        length_first_word, length_second_word = length_second_word, length_first_word
    current_row = list(range(length_first_word + 1))
    for item in range(1, length_second_word + 1):
        previous_row, current_row = current_row, [item] + [0] * length_first_word
        for _item in range(1, length_first_word + 1):
            add = previous_row[_item] + 1
            delete = current_row[_item - 1] + 1
            change = previous_row[_item - 1]
            if first_word[_item - 1] != second_word[item - 1]:
                change += 1
            current_row[_item] = min(add, delete, change)
    return current_row[length_first_word]


def soundex(string):
    first_symbol = string[0].upper()
    string = string[1:]
    string = re.sub('[hw]', '', string, flags=re.I)
    string = re.sub('[bfpv]+', '1', string, flags=re.I)
    string = re.sub('[cgjkqsxz]+', '2', string, flags=re.I)
    string = re.sub('[dt]+', '3', string, flags=re.I)
    string = re.sub('l+', '4', string, flags=re.I)
    string = re.sub('[mn]+', '5', string, flags=re.I)
    string = re.sub('r+', '6', string, flags=re.I)
    string = re.sub('[aeiouy]', '', string, flags=re.I)
    result = ''.join((first_symbol, string[0:3]))
    return result.ljust(4, '0')
