import sys

from game import RANKS

def card_rank(card):
    return 14 - RANKS[-1::-1].index(card['rank'])

class Preflop:
    def __init__(self, game_state):
        player = game_state['players'][game_state['in_action']]
        self.hole_cards = player['hole_cards']

    def name(self):
        c1=self.hole_cards[0];
        cr1= card_rank(c1);
        c2 = self.hole_cards[1]
        cr2=card_rank(c2);
        if cr1 == cr2:
            return 'Pair of {rank}'.format(rank=self.hole_cards[0]['rank'])

        if cr2>cr1:
            high_card=c2
            low_card=c1
        else:
            high_card = c1
            low_card = c2

        return 'High card {r1}, low card {r2}'.format(r1=high_card['rank'], r2=low_card['rank'])
