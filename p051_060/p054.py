from __future__ import annotations
from enum import Enum
from functools import total_ordering

P054_poker_hands = [(line[0: 14], line[15:])
                    for line in open('constant_inputs/p054_input.txt')]


def p054(input: list[tuple[str, str]] = P054_poker_hands) -> int:
    return sum(PokerHand(hand1).can_win(PokerHand(hand2)) for (hand1, hand2) in input)


@total_ordering
class Rank(Enum):
    HighCard = 1
    OnePair = 2
    TwoPairs = 3
    ThreeOfAKind = 4
    Straight = 5
    Flush = 6
    FullHouse = 7
    FourOfAKind = 8
    StraightFlush = 9
    RoyalFlush = 10

    def __lt__(self, other: Rank):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


Card_Value = "0023456789TJQKA"


class PokerHand:
    def __init__(self, hand: str):
        self.cards = hand.split(" ")
        self.hand = sorted(
            (Card_Value.index(card[0]) for card in self.cards), reverse=True)
        self.kind_set = set(self.hand)
        self.rank_values = self.sort_kinds_by_freq()
        self.score = self.determine_rank(), self.rank_values

    def __str__(self):
        return f'{self.score}'

    def check_flush(self) -> bool:
        return len(set(card[1] for card in self.cards)) == 1

    def check_straight(self) -> bool:
        # hands are already sorted desc before checking rank,
        # so check each card to be bigger than next card by 1
        return all(self.hand[i] == self.hand[i + 1] + 1 for i in range(4))

    def check_four_cards(self) -> bool:
        most_freq_card = self.rank_values[0]
        return self.hand.count(most_freq_card) == 4

    def check_three_cards(self) -> bool:
        most_freq_card = self.rank_values[0]
        return self.hand.count(most_freq_card) == 3

    def sort_kinds_by_freq(self) -> list[int]:
        # return the kind value sorted by frequency in desc order.
        # if same freq, sort by card value in desc order
        # use for comparing same rank cases e.g. Full House vs Full House.
        return sorted(self.kind_set, key=lambda kind: (self.hand.count(kind), kind), reverse=True)

    def determine_rank(self) -> Rank:
        is_flush = self.check_flush()
        is_straight = self.check_straight()

        if is_straight:
            if is_flush:
                if max(self.hand) == 14:
                    return Rank.RoyalFlush
                else:
                    return Rank.StraightFlush
            else:
                return Rank.Straight

        elif len(self.kind_set) == 2:
            # only two kinds of cards, so it must be four of a kind or full house
            if self.check_four_cards():
                return Rank.FourOfAKind
            else:
                return Rank.FullHouse

        elif is_flush:
            return Rank.Flush

        elif len(self.kind_set) == 3:
            # must be three of a kind or two pairs
            if self.check_three_cards():
                return Rank.ThreeOfAKind
            else:
                return Rank.TwoPairs

        elif len(self.kind_set) == 4:
            return Rank.OnePair
        else:
            return Rank.HighCard

    def can_win(self, other: PokerHand) -> bool:
        return self.score > other.score
