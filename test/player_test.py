import unittest

from player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_(self):
        result = self.player.betRequest(dict(
            current_buy_in=250,
            minimum_raise=1,
            in_action=0,
            players=[
                dict(
                    hole_cards=[
                        dict(rank='A', suit='hearts'),
                        dict(rank='K', suit='hearts'),
                    ],
                    bet=250,
                    stack=1000,
                )
            ],
            community_cards=[],
        ))

        print result

