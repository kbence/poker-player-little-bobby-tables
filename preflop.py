import sys

class Preflop:
    def __init__(self, game_state):
        player = game_state['players'][game_state['in_action']]
        hole_cards = player['hole_cards']

    def name(self):
        return "Pair of A"
