
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
        return self._player['hole_cards']


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
        return self._game_state['community_cards']

