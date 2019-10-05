import unittest
from preflop import Preflop

def mock_card(card):
    return {'rank': card[0:1], 'suit': card[1:2]}

def mock_hole_cards(cards):
    return [mock_card(card) for card in cards]

class I_can_has_unittest(unittest.TestCase):

    # diamonds clubs hearts spades
    def mock_hole(self, cards):
        game={
            'in_action':'dummy',
            'players':{'dummy':{
                'hole_cards': mock_hole_cards(cards)
            }}
        }
        return game

    def test_preflop_class(self):
        x=Preflop(self.mock_hole(["AD", "2H"]))
        self.assertIsInstance(x, Preflop)

    def test_name_pair_A(self):
        x=Preflop(self.mock_hole(["AD", "AD"]))
        self.assertEqual(x.name(), "Pair of A")

    def test_name_pair_K(self):
        x=Preflop(self.mock_hole(["KD", "KD"]))
        self.assertEqual(x.name(), "Pair of K")

    def test_name_high_A(self):
        x=Preflop(self.mock_hole(["AD", "KD"]))
        self.assertEqual(x.name(), "High card A, low card K")
