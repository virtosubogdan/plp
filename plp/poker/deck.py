from random import shuffle


def compare_cards(card1, card2):
    if card1.color is card2.color:
        cmp(card1.number, card2.number)
    return cmp(card1.color, card2.color)


class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __repr__(self):
        return '{' + self.color + str(self.number) + '}'


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def add_cards(self, cards):
        self.cards.extend(cards)

    def remove_card(self, card):
        return self.cards.remove(card)

    def pop(self):
        return self.cards.pop()

    def shuffle_cards(self):
        shuffle(self.cards)

    def order_cards(self):
        self.cards.sort(compare_cards)
