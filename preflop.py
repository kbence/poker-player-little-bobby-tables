import sys
from math import ceil

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

    def is_pair(self):
        c1=self.hole_cards[0]
        cr1= card_rank(c1)
        c2 = self.hole_cards[1]
        cr2=card_rank(c2)
        return cr1 == cr2

    def name(self):
        c1=self.hole_cards[0]
        cr1= card_rank(c1)
        c2 = self.hole_cards[1]
        cr2=card_rank(c2)
        if self.is_pair():
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

    def is_same_suit(self):
        return self.hole_cards[0]['suit']==self.hole_cards[1]['suit']

    def rank_diff_score_correction(self):
        c1=self.hole_cards[0]
        cr1= card_rank(c1)
        c2 = self.hole_cards[1]
        cr2=card_rank(c2)
        return min(5,abs(cr2-cr1))

    def score(self):
        return ceil(self.high_card_value() * (2 if self.is_pair() else 1) + (2 if self.is_same_suit() else 0) - self.rank_diff_score_correction())
