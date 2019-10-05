import sys

from game import RANKS

def card_rank(card):
    return 14 - RANKS[-1::-1].index(card['rank'])

class Preflop:
    def __init__(self, game_state):
        player = game_state['players'][game_state['in_action']]
        self.hole_cards = player['hole_cards']

    def high_card(self):
        c1=self.hole_cards[0]
        cr1 = card_rank(c1)
        c2 = self.hole_cards[1]
        cr2 =card_rank(c2)
        if(cr1>=cr2):
            return c1
        return c2

    def name(self):
        c1=self.hole_cards[0]
        cr1= card_rank(c1)
        c2 = self.hole_cards[1]
        cr2=card_rank(c2)
        if cr1 == cr2:
            return 'Pair of {rank}'.format(rank=self.hole_cards[0]['rank'])

        if cr2>cr1:
            low_card=c1
        else:
            low_card = c2

        return 'High card {r1}, low card {r2}'.format(r1=self.high_card()['rank'], r2=low_card['rank'])

    high_card_values=[-666, -42, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10]
    def high_card_value(self):
        r = card_rank(self.high_card())
        return self.high_card_values[r]
