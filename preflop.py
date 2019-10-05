import sys

class Preflop:
    def __init__(self, game_state):
        player = game_state['players'][game_state['in_action']]
        self.hole_cards = player['hole_cards']

    def name(self):
        r1=self.hole_cards[0]['rank'];
        r2=self.hole_cards[1]['rank'];
        if r1 == r2:
            return 'Pair of {rank}'.format(rank=self.hole_cards[0]['rank'])

        return 'High card {r1}, low card {r2}'.format(r1=r1, r2=r2)
