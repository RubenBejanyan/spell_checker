import io
from utils import levenshtein_distance as lev_dis
from utils import soundex as soundex


def spelling_assistant(word):
    soundex_code = soundex(word)
    with io.open('dictionary.txt') as mf:
        same_soundex = [line[:-1] for line in mf if soundex_code == soundex(line)]
    return [elem for elem in same_soundex if lev_dis(elem, word) == min([lev_dis(x, word) for x in same_soundex])]
