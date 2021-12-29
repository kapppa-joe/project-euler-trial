from string import ascii_uppercase as Letters
import pathlib
import itertools
import re

from util import triangle_number_generator


P042_words_list_raw = pathlib.Path(
    'constant_inputs/p042_words.txt').read_text()
P042_words_list = [word for word in re.findall(
    r'"(\w+)"', P042_words_list_raw)]

Triangle_numbers = list(itertools.takewhile(
    lambda t: t < 10000, triangle_number_generator()))


def is_triangle_number(num: int) -> bool:
    if num >= 10000:
        raise ValueError('this function only support numbers below 10000')
    return num in Triangle_numbers


def word_value(word: str) -> int:
    return sum(Letters.index(char) + 1 for char in word)


def p042(words_list: list[str] = P042_words_list) -> int:
    """ The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
    """
    return sum(1 for word in words_list if is_triangle_number(word_value(word)))
