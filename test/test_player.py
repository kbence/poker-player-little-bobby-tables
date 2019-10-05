import unittest

from player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        super(PlayerTest, self).setUp()
        self.player = Player()

    def create_game_state(self, **kwargs):
        player_patch = dict()

        for field in ['hole_cards', 'bet', 'stack']:
            if field in kwargs:
                player_patch[field] = kwargs[field]
                del kwargs[field]

        game_state = dict(
            game_id='82374628375618542385',
            current_buy_in=250,
            minimum_raise=10,
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
        )

        game_state['players'][game_state['in_action']].update(player_patch)
        game_state.update(**kwargs)

        return game_state

    def test_checks(self):
        result = self.player.betRequest(self.create_game_state(current_buy_in=150, bet=50))

        self.assertIsInstance(result, int)
        self.assertEqual(result, 100)

    def test_folds_on_high_stacks(self):
        result = self.player.betRequest(self.create_game_state())

        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_goes_all_in_for_high_pair(self):
        result = self.player.betRequest(self.create_game_state(
            hole_cards=[dict(rank='A', suit='hearts'), dict(rank='A', suit='diamonds')]
        ))

        self.assertIsInstance(result, int)
        self.assertEqual(result, 1000)

    def test_fold_with_high_cards_and_high_stakes(self):
        result = self.player.betRequest(self.create_game_state(
            hole_cards=[dict(rank='A', suit='hearts'), dict(rank='K', suit='diamonds')],
            current_buy_in=600,
            bet=50,
        ))

        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)
