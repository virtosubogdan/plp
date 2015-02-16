import unittest
from plp.poker.dealer import Dealer, Player
from plp.poker.deck import Deck, Card


class TestPoker(unittest.TestCase):
    def make_deck(self):
        deck = Deck()
        for color in ['S', 'H', 'D', 'C']:
            for number in range(1, 15):
                deck.add_card(Card(color, number))
        return deck

    def test_let_s_play_a_game(self):
        deck = self.make_deck()
        dealer = Dealer()
        p1 = Player('Bob')
        p2 = Player('Kate')
        dealer.add_player(p1)
        dealer.add_player(p2)
        dealer.set_deck(deck)
        dealer.deal()
        dealer.remove_player(p1)
        dealer.stop_game()
        self.assertEqual(len(dealer.remove_deck().cards), 56)
