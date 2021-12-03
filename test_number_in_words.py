from number_in_words import count_letters, number_in_words, lookup_table


def test_number_in_words():
    assert number_in_words(1) == 'one'
    assert number_in_words(2) == 'two'
    assert number_in_words(3) == 'three'
    assert number_in_words(4) == 'four'

    for i in range(5, 21):
        assert number_in_words(i) == lookup_table[i]

    assert number_in_words(21) == 'twenty one'
    assert number_in_words(47) == 'forty seven'
    assert number_in_words(70) == 'seventy'
    assert number_in_words(92) == 'ninety two'

    assert number_in_words(100) == 'one hundred'
    assert number_in_words(101) == 'one hundred and one'
    assert number_in_words(342) == 'three hundred and forty two'
    assert number_in_words(1000) == 'one thousand'
    assert number_in_words(2021) == 'two thousand and twenty one'
    assert number_in_words(2345) == 'two thousand three hundred and forty five'


def test_count_letters():
    assert count_letters('') == 0
    assert count_letters('apple') == 5
    assert count_letters('jam and bread') == 11  # ignore whitespace
