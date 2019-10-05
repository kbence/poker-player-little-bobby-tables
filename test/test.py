import unittest
from preflop import Preflop

class I_can_has_unittest(unittest.TestCase):

    # diamonds clubs hearts spades
    def mock_hole(self, cards):
        game={
            'in_action':'dummy',
            'players':{'dummy':{
                'hole_cards':[
                    {'rank':'A',
                     'suit':'hearts'}
                ]
            }}
        }

        return game

    def test_preflop_class(self):
        x=Preflop(self.mock_hole(["AD", "2H"]))
        self.assertIsInstance(x, Preflop)

    def test_name(self):
        x=Preflop(self.mock_hole(["AD", "AD"]))
        self.assertEqual(x.name(), "Pair of A")
