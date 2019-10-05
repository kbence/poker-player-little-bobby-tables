
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]

class Player:
    def __init__(self, player):
        self._player = player

    @property
    def bet(self):
        return self._player['bet']

    @property
    def stack(self):
        return self._player['stack']

    @property
    def hole_cards(self):
        return [Card(card) for card in self._player['hole_cards']]


class Card:
    def __init__(self, card):
        self._card = card

    @property
    def rank(self):
        return self._card['rank']

    @property
    def rank_value(self):
        return 14 - RANKS[-1::-1].index(self.rank)

    @property
    def suit(self):
        return self._card['suit']


class GameState:
    def __init__(self, game_state):
        self._game_state = game_state

    @property
    def current_buy_in(self):
        return self._player['current_buy_in']

    @property
    def minimum_raise(self):
        return self._player['minimum_raise']

    @property
    def our_player(self):
        return self._game_state['players'][self._game_state['in_action']]

    @property
    def community_cards(self):
        return [Card(card) for card in self._game_state['community_cards']]
