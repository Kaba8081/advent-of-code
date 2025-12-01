# 'Advent of code' solution for year 2023 day 7
import os
import sys

from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
                        
global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def get_input() -> list:
    input = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r") as file:    
            input = file.read().strip().splitlines()
        return input
    else:
        print("Error! Input file does not exist!")
        sys.exit()

class CardType(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OAK = 3
    FULL_HOUSE = 4
    FOUR_OAK = 5
    FIVE_OAK = 6

@dataclass
class Card:
    value: str
    type: CardType
    bet: int
    rank: int

    def __str__(self) -> str:
        return f"{self.value} {self.type} {self.bet} {self.rank}"
    
    def rankCard(self, cards_list: list, part: int) -> None:
        cards_list.remove(self) # remove self from list
        
        # rank = count of worse cards + 1 
        count = 0
        points = {}
        values = []
        if part == 1:
            values = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
        else:
            values = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")

        for i in range(len(values)): points[values[i]] = len(values) - i

        for card in cards_list:
            if self.type > card.type:
                count += 1
            elif card.type == self.type: # check every letter until one card is better
                for index, letter in enumerate(self.value):
                    if points[letter] > points[card.value[index]]:
                        count += 1
                        break
                    elif points[letter] == points[card.value[index]]:
                        continue
                    else:
                        break
        self.rank = count + 1

def checkCard(card: str) -> CardType:
    # Five of a kind, where all five cards have the same label: AAAAA
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # High card, where all cards' labels are distinct: 23456

    symbols = list(set(card.upper()))

    if len(symbols) == 1:
        return CardType.FIVE_OAK # Five of a kind
    elif len(symbols) == 2:
        if card.count(symbols[0]) == 4 or card.count(symbols[1]) == 4:
            return CardType.FOUR_OAK # Four of a kind
        else:
            return CardType.FULL_HOUSE # Full house
    elif len(symbols) == 3:
        if card.count(symbols[0]) == 3 or card.count(symbols[1]) == 3 or card.count(symbols[2]) == 3:
            return CardType.THREE_OAK # Three of a kind
        else:
            return CardType.TWO_PAIR # Two pair
    elif len(symbols) == 4:
        return CardType.ONE_PAIR # One pair
    else:
        return CardType.HIGH_CARD # High card
    
def part1(input: list) -> int:
    """check type of each card -> rank cards -> sum ranks * bet"""
    cards = []

    for line in input:
        card, bet = line.split(" ")
        type = checkCard(card)
        cards.append(Card(card, type, int(bet), 0))
    
    for card in cards:
        card.rankCard(cards.copy(), 1)

    return sum(card.rank * card.bet for card in cards)

def checkCardWithJokers(card: str) -> CardType:
    counter = Counter(card.upper())
    highest = max(counter.values())

    wilds = counter["J"]
    del counter["J"]
    highest = wilds
    if counter: 
         highest += max(counter.values())

    if highest == 5:
        return CardType.FIVE_OAK # Five of a kind
    elif highest == 4:
        return CardType.FOUR_OAK # Four of a kind
    elif len(counter) == 2:
        return CardType.FULL_HOUSE # Full house
    elif highest == 3:
        return CardType.THREE_OAK # Three of a kind
    elif len(counter) == 3:
        return CardType.TWO_PAIR # Two pair
    elif highest == 2:
        return CardType.ONE_PAIR # One pair
    else:
        return CardType.HIGH_CARD # High card
        
def part2(input: list) -> int:
    """check type of each card -> rank cards -> sum ranks * bet"""
    cards = []

    for line in input:
        card, bet = line.split(" ")
        type = checkCardWithJokers(card)
        cards.append(Card(card, type, int(bet), 0))
    
    for card in cards:
        card.rankCard(cards.copy(), 2)

    return sum(card.rank * card.bet for card in cards)

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()
                        
    input1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".strip().splitlines()
    
    result1 = part1(input)
    print("[7.1] Sum of all bets x ranks: ", result1)
    result2 = part2(input)
    print("[7.2] Sum of all winnings: ", result2)
    sys.exit()
