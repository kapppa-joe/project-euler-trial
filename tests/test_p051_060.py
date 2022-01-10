import pytest

from p051_060.p051 import determine_same_digit_group, same_digit
from p051_060.p052 import are_permutation, has_n_permuted_multiples
from p051_060.p053 import p053
from p051_060.p054 import PokerHand, Rank


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
