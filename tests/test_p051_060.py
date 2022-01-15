import pytest
import numpy as np

from p051_060.p051 import determine_same_digit_group, same_digit
from p051_060.p052 import are_permutation, has_n_permuted_multiples
from p051_060.p053 import p053
from p051_060.p054 import PokerHand, Rank
from p051_060.p055 import check_lychrel, reverse_add
from p051_060.p056 import p056
from p051_060.p057 import fraction_seq, p057
from p051_060.p058 import p058, spiral_diagonal_generator
from p051_060.p059 import Key_Combinations, can_find_words_in_text, looks_like_english
from p051_060.p060 import check_prime_pair, p060, search_graph_for_pairs_set, update_graph
from util import all_primes_below


def test_p051_same_digit_group():
    pool = set([1234, 1123, 1334, 4423, 1444, 1554])
    output = determine_same_digit_group(pool)
    assert output == {'**23': {1123, 4423},
                      '1**4': {1334, 1444, 1554},
                      '1***': {1444}}


def test_p051_same_digit():
    assert same_digit(1234) == set()
    assert same_digit(1223) == {'2'}
    assert same_digit(56003) == {'0'}
    assert same_digit(56006) == {'0', '6'}


def test_p052_are_permutation():
    assert are_permutation(1, 2) == False
    assert are_permutation(12, 21) == True
    assert are_permutation(1223, 1332) == False
    assert are_permutation(1223, 1232) == True
    assert are_permutation(12340, 4321) == False
    assert are_permutation(125874, 251748) == True


def test_p052_has_n_permuted_multiples():
    assert has_n_permuted_multiples(125874, 2) == True


def test_p053():
    assert p053(22) == 0
    assert p053(23) == 4


def test_p054_check_flush():
    hand1 = PokerHand("3D 6D 7D TD QD")
    assert hand1.check_flush() == True
    assert hand1.score == (Rank.Flush, [12, 10, 7, 6, 3])
    assert PokerHand("3H 6D 7D TD QD").check_flush() == False


def test_p054_check_straight():
    hand1 = PokerHand("JC 9S TH 8D 7H")
    hand2 = PokerHand("6H 4H 5C 3H 2H")
    assert hand1.check_straight() == True
    assert hand2.check_straight() == True
    assert hand1.score == (Rank.Straight, [11, 10, 9, 8, 7])
    assert hand2.score == (Rank.Straight, [6, 5, 4, 3, 2])
    assert PokerHand("2D 3D 4D 5D 7D").check_straight() == False


def test_p054_check_straight_flush():
    hand1 = PokerHand("JH 9H TH 8H 7H")
    assert hand1.score == (Rank.StraightFlush, [11, 10, 9, 8, 7])


def test_p054_check_royal_flush():
    hand1 = PokerHand("JH KH TH AH QH")
    assert hand1.score[0] == Rank.RoyalFlush


def test_p054_check_full_house():
    hand1 = PokerHand("2H 2D 4C 4D 4S")
    hand2 = PokerHand("3C 3D 3S 9S 9D")
    assert hand1.score == (Rank.FullHouse, [4, 2])
    assert hand2.score == (Rank.FullHouse, [3, 9])
    assert hand1.can_win(hand2) == True


def test_p054_check_four_cards():
    hand1 = PokerHand("AD 3D 3S 3H 3C")
    hand2 = PokerHand("TC 5H 5S 5D 5C")
    assert hand1.score == (Rank.FourOfAKind, [3, 14])
    assert hand2.score == (Rank.FourOfAKind, [5, 10])
    assert hand1.can_win(hand2) == False


def test_p054_check_three_cards():
    hand1 = PokerHand("2D 9C AS AH AC")
    hand2 = PokerHand("2D AC TS TH TC")
    assert hand1.score == (Rank.ThreeOfAKind, [14, 9, 2])
    assert hand2.score == (Rank.ThreeOfAKind, [10, 14, 2])


def test_p054_check_two_pairs():
    hand1 = PokerHand("AD 2H AH 6D 2S")
    hand2 = PokerHand("KD KH 7H QD QS")
    assert hand1.score == (Rank.TwoPairs, [14, 2, 6])
    assert hand2.score == (Rank.TwoPairs, [13, 12, 7])


def test_p054_check_one_pair():
    hand1 = PokerHand("5H 5C 6S 7S KD")
    hand2 = PokerHand("2C 3S 8S 8D TD")
    assert hand1.score == (Rank.OnePair, [5, 13, 7, 6])
    assert hand2.score == (Rank.OnePair, [8, 10, 3, 2])


Test_cases_P054 = [
    # hand1_cards, hand2_cards,
    # player1_wins,
    # hand1_rank, hand2_rank, hand1_rank_value, hand2_rank_value
    ("5H 5C 6S 7S KD", "2C 3S 8S 8D TD",
     False,
     Rank.OnePair, Rank.OnePair, [5, 13, 7, 6], [8, 10, 3, 2]),
    ("5D 8C 9S JS AC", "2C 5C 7D 8S QH",
     True,
     Rank.HighCard, Rank.HighCard, [14, 11, 9, 8, 5], [12, 8, 7, 5, 2]),
    ("2D 9C AS AH AC", "3D 6D 7D TD QD",
     False,
     Rank.ThreeOfAKind, Rank.Flush, [14, 9, 2], [12, 10, 7, 6, 3]),
    ("4D 6S 9H QH QC", "3D 6D 7H QD QS",
     True,
     Rank.OnePair, Rank.OnePair, [12, 9, 6, 4], [12, 7, 6, 3]),
    ("2H 2D 4C 4D 4S", "3C 3D 3S 9S 9D",
     True,
     Rank.FullHouse, Rank.FullHouse, [4, 2], [3, 9]),
]


@pytest.mark.parametrize("hand1_cards, hand2_cards, player1_wins, hand1_rank, hand2_rank, hand1_rank_value, hand2_rank_value", Test_cases_P054)
def test_p054_compare_hands(hand1_cards, hand2_cards, player1_wins, hand1_rank, hand2_rank, hand1_rank_value, hand2_rank_value):
    hand1 = PokerHand(hand1_cards)
    hand2 = PokerHand(hand2_cards)
    assert hand1.can_win(hand2) == player1_wins
    assert hand1.score[0] == hand1_rank
    assert hand2.score[0] == hand2_rank
    assert hand1.score[1] == hand1_rank_value
    assert hand2.score[1] == hand2_rank_value


def test_p055_reverse_add():
    assert reverse_add(47) == 121
    assert reverse_add(349) == 1292
    assert reverse_add(1292) == 4213
    assert reverse_add(4213) == 7337


def test_p055_check_lychrel():
    assert check_lychrel(47) == False
    assert check_lychrel(74) == False
    assert check_lychrel(196) == True
    assert check_lychrel(349) == False
    assert check_lychrel(4994) == True


def test_p056():
    assert p056(3, 3) == 4
    assert p056(4, 4) == 9
    assert p056(10, 10) == 45  # 9 ** 9
    assert p056(20, 20) == 127


def test_p057_fraction_seq():
    assert fraction_seq(1) == (3, 2)
    assert fraction_seq(2) == (7, 5)
    assert fraction_seq(3) == (17, 12)
    assert fraction_seq(4) == (41, 29)
    assert fraction_seq(5) == (99, 70)
    assert fraction_seq(6) == (239, 169)
    assert fraction_seq(7) == (577, 408)
    assert fraction_seq(8) == (1393, 985)


def test_p057():
    assert p057(7) == 0
    assert p057(8) == 1
    assert p057(12) == 1
    assert p057(13) == 2  # 13th is (114243, 80782)


def test_p058_spiral_generator():
    gen = spiral_diagonal_generator()
    assert next(gen) == (1,)
    assert next(gen) == (3, 5, 7, 9)
    assert next(gen) == (13, 17, 21, 25)
    assert next(gen) == (31, 37, 43, 49)


def test_p058():
    assert p058(0.61) == 3
    assert p058(0.56) == 5  # 5 in 9 are primes for side length = 5


def test_p059_key_combinations():
    keys_generated = list(Key_Combinations)
    assert len(keys_generated) == 26 ** 3
    assert tuple(ord(char) for char in 'abc') in keys_generated
    assert tuple(ord(char) for char in 'aaa') in keys_generated
    assert tuple(ord(char) for char in 'cat') in keys_generated
    assert tuple(ord(char) for char in 'zyx') in keys_generated
    assert tuple(ord(char) for char in 'xyz') in keys_generated
    assert tuple(ord(char) for char in 'Abc') not in keys_generated


def test_p059_looks_like_english():
    text = 'Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.'
    text_arr = np.array([ord(char) for char in text])
    assert looks_like_english(text_arr) >= 100

    text = 'For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.'
    text_arr = np.array([ord(char) for char in text])
    assert looks_like_english(text_arr) >= 100

    text = 'dsdsjdijj!(#($%(HNfofkm dfdm  fldksdsjidajidj9u91 u1u9a9dwdjidji dwi0iew0djsnixu9s99!'
    text_arr = np.array([ord(char) for char in text])
    assert looks_like_english(text_arr) == 0


def test_p059_find_words_in_text():
    text = 'Your task has been made easy, as the encryption key consists of three lower case characters.'
    text_arr = np.array([ord(char) for char in text])
    assert can_find_words_in_text(
        text_arr, ["task", "has", "been", "made", "difficult"]) == 4
    assert can_find_words_in_text(text_arr, ["no", "such", "words"]) == 0


def test_p060_check_prime_pair():
    assert check_prime_pair(3, 7) == True
    assert check_prime_pair(2, 7) == False
    assert check_prime_pair(17, 23) == False
    assert check_prime_pair(3, 109) == True
    assert check_prime_pair(3, 673) == True
    assert check_prime_pair(109, 673) == True


def test_p060_update_graph():
    graph = {}
    for p in all_primes_below(20):
        graph = update_graph(p, graph)
    assert graph == {2: set(), 3: {7, 11, 17}, 5: set(), 7: {3, 19},
                     11: {3}, 13: {19},  17: {3}, 19: {13, 7}}


def test_search_graph_for_pairs_set():

    # try search for a set of 2 primes for n < 10
    graph = {}
    for p in all_primes_below(10):
        graph = update_graph(p, graph)
    output = search_graph_for_pairs_set(
        graph=graph, wanted_size=2, curr_node=3)
    assert output == {3, 7}

    output2 = search_graph_for_pairs_set(
        graph=graph, wanted_size=2, curr_node=2)
    assert output2 == None  # no such groups found for 2

    # try search for a set of 3 primes for n < 100
    graph = {}
    for p in all_primes_below(100):
        graph = update_graph(p, graph)
    output3 = search_graph_for_pairs_set(
        graph=graph, wanted_size=3, curr_node=3)
    assert output3 == {3, 37, 67}

    # try search for a set of 4 primes for n < 1000
    graph = {}
    for p in all_primes_below(1000):
        graph = update_graph(p, graph)
    output4 = search_graph_for_pairs_set(
        graph=graph, wanted_size=4, curr_node=3)
    assert output4 == {3, 7, 109, 673}


def test_p060():
    assert p060(set_size=2) == sum({3, 7})
    assert p060(set_size=3) == sum({3, 37, 67})
    assert p060(set_size=4) == sum({3, 7, 109, 673})
    assert p060(set_size=5) == sum({13, 5197, 5701, 6733, 8389})
