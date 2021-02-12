from utils import levenshtein_distance as lev_dis
from utils import soundex as soundex
from operator import itemgetter


def my_gen(file, word):
    first_letter = word[0]
    soundex_code = soundex(word)
    with open(file) as mf:
        for line in mf:
            if first_letter == line[0]:
                _line = line[:-1]
                if soundex_code == soundex(_line):
                    yield line[:-1], lev_dis(word, _line)


def spelling_assistant(word):
    my_list = [x for x in my_gen('dictionary.txt', word)]
    min_lev = min(my_list, key=itemgetter(1))[1]
    res = [x for x, y in my_list if y == min_lev]
    return res
