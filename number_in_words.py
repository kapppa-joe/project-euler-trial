from functools import cache

lookup_table = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred'
}


@cache
def number_in_words(n: int) -> str:
    """
    return the number in words. e.g. 342 -> three hundred and forty two
    """
    if n <= 0:
        return ''
    elif n > 0 and n < 21:
        return lookup_table[n]
    elif n < 100:
        ones = n % 10
        tens = n - ones
        if ones == 0:
            return lookup_table[tens]
        else:
            return f'{lookup_table[tens]} {number_in_words(ones)}'
    elif n < 1000:
        hundreds = n // 100
        balance = n % 100
        if balance == 0:
            return f'{number_in_words(hundreds)} hundred'
        else:
            return f'{number_in_words(hundreds)} hundred and {number_in_words(balance)}'
    elif n < 1_000_000:
        thousands = n // 1_000
        balance = n % 1_000
        if balance == 0:
            return f'{number_in_words(thousands)} thousand'
        elif balance < 100:
            return f'{number_in_words(thousands)} thousand and {number_in_words(balance)}'
        else:
            return f'{number_in_words(thousands)} thousand {number_in_words(balance)}'

    return ''


def count_letters(string: str) -> int:
    return len(string.replace(' ', ''))
