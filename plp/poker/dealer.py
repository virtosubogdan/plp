class Player:
    def __init__(self, name):
        self.cards = []
        self.name = name

    def give_card(self, card):
        self.cards.append(card)

    def take_cards(self):
        temp, self.cards = self.cards, []
        return temp

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.name == other.name)


class Dealer:
    def __init__(self):
        self.deck = None
        self.players = set()
        self.is_game_on = False
        self.discarded_cards = []
        self.table_cards = []

    def __assert_game_off(self):
        if self.is_game_on:
            raise RuntimeWarning('Game is Running')

    def set_deck(self, deck):
        self.__assert_game_off()
        if self.deck is not None:
            raise RuntimeError('Deck already set')
        self.deck = deck

    def remove_deck(self):
        self.__assert_game_off()
        temp, self.deck = self.deck, None
        return temp

    def add_player(self, player):
        self.__assert_game_off()
        self.players.add(player)

    def remove_player(self, player):
        self.discarded_cards.extend(player.take_cards())
        self.players.remove(player)

    def deal(self):
        self.__assert_game_off()
        self.deck.shuffle_cards()
        for i in range(2):
            for player in self.players:
                player.give_card(self.deck.pop())
        for i in range(5):
            self.table_cards.append(self.deck.pop())
        self.is_game_on = True

    def stop_game(self):
        self.deck.add_cards(self.discarded_cards)
        self.deck.add_cards(self.table_cards)
        self.discarded_cards, self.table_cards = [], []
        for player in self.players:
            self.deck.add_cards(player.take_cards())
        self.deck.order_cards()
        self.is_game_on = False
