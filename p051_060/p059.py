import numpy as np
from numpy.typing import NDArray
import itertools
import string

P059_Encrypted_Text = np.array([int(num_str) for num_str in open(
    'constant_inputs/p059_cipher.txt').read().split(',')])

a_to_z = [ord(char) for char in string.ascii_lowercase]
Key_Combinations = itertools.product(a_to_z, repeat=3)

Common_english_chars = set(ord(char) for char in (
    string.ascii_letters + string.digits + string.punctuation + ' '))

# Common_english_chars.update(range(ord('A'), ord('Z') + 1))
# Common_english_chars.update(range(ord('0'), ord('9') + 1))
# Common_english_chars.update(ord(char) for char in ' .,;()[]{}"\'+-*/')


def p059(raw_text=P059_Encrypted_Text):
    decryption_trials = (try_decrypt(raw_text, key)
                         for key in Key_Combinations)
    candidate = max(decryption_trials, key=looks_like_english)
    print(''.join(chr(c) for c in candidate))
    return candidate.sum()


def try_decrypt(raw_text: NDArray, key: tuple[int]) -> NDArray:
    padded_key = np.resize(key, len(raw_text))
    return raw_text ^ padded_key


def looks_like_english(text: NDArray) -> int:
    # score a decrypted text by how much it looks similar to common English.
    score = 0

    chars, freq = np.unique(text, return_counts=True)
    chars_sorted_by_freq_desc = chars[np.argsort(freq)[::-1]]

    # give 10 points according to letter frequency
    top_ten_most_freq_chars_in_text = chars_sorted_by_freq_desc[:10]
    for char in top_ten_most_freq_chars_in_text:
        if char in [ord(c) for c in "etainoshrd"]:
            # "etainoshrd" : top 10 most freq letters in common English
            score += 10

    if score < 50:
        return min(0, score)

    # give points if common English words can be found in the text
    score += can_find_words_in_text(text,
                                    ["the", "to", "of", "and", "that", "have", "for", "not", "with", "you", "this", "but"]) * 10
    if score < 100:
        return min(0, score)

    # deduct score for each char in text that are not Common English chars
    for char in chars:
        if not char in Common_english_chars:
            score -= 5

    return score


def can_find_words_in_text(text: NDArray, words: list[str]) -> int:
    # count how many of specified words can be found in given text array
    text_str = ''.join(chr(c) for c in text)
    return sum(word in text_str for word in words)
