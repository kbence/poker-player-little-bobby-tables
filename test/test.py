import unittest
from preflop import Preflop

class I_can_has_unittest(unittest.TestCase):

    def test_preflop_class(self):
        x=Preflop()
        self.assertIsInstance(x, Preflop)
