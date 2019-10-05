import unittest
from preflop import Preflop, card_rank


def mock_card(card):
    return {'rank': card[0:-1], 'suit': card[-2:-1]}

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

    def test_name_high_A_rev(self):
        x=Preflop(self.mock_hole(["KD", "AD"]))
        self.assertEqual("High card A, low card K", x.name())

    ######################################################

    def test_card_rank_A(self):
        self.assertEqual(card_rank({'rank':'A'}), 14)

    def test_high_value_A(self):
        self.assertEqual(10, Preflop(self.mock_hole(["AD", "2D"])).high_card_value())

    def test_high_value_K(self):
        self.assertEqual(8, Preflop(self.mock_hole(["KD", "2D"])).high_card_value())

    def test_high_value_Q(self):
        self.assertEqual(7, Preflop(self.mock_hole(["QD", "2D"])).high_card_value())

    def test_high_value_J(self):
        self.assertEqual(6, Preflop(self.mock_hole(["JD", "2D"])).high_card_value())

    def test_high_value_10(self):
        self.assertEqual(5, Preflop(self.mock_hole(["10D", "2D"])).high_card_value())

    def test_high_value_9(self):
        self.assertEqual(4.5, Preflop(self.mock_hole(["9D", "2D"])).high_card_value())

    def test_high_value_8(self):
        self.assertEqual(4, Preflop(self.mock_hole(["8D", "2D"])).high_card_value())

    def test_high_value_7(self):
        self.assertEqual(3.5, Preflop(self.mock_hole(["7D", "2D"])).high_card_value())

    def test_high_value_6(self):
        self.assertEqual(3, Preflop(self.mock_hole(["6D", "2D"])).high_card_value())

    def test_high_value_5(self):
        self.assertEqual(2.5, Preflop(self.mock_hole(["5D", "2D"])).high_card_value())

    def test_high_value_4(self):
        self.assertEqual(2, Preflop(self.mock_hole(["4D", "2D"])).high_card_value())

    def test_high_value_3(self):
        self.assertEqual(1.5, Preflop(self.mock_hole(["3D", "2D"])).high_card_value())

    def test_high_value_2(self):
        self.assertEqual(1, Preflop(self.mock_hole(["2D", "2D"])).high_card_value())
