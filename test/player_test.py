import unittest

from player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_(self):
        self.player.betRequest(dict(
            current_buy_in=0,
            minimum_raise=1,
            in_action=0,
            players=[
                dict(
                    hole_cards=[
                        dict(rank='A', suit='hearts'),
                        dict(rank='K', suit='hearts'),
                    ],
                    bet=1,
                    stack=1,
                )
            ],
            community_cards=[],
        ))

