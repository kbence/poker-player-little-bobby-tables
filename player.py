import json

from game import GameState


class Player:
    VERSION = "Rampage bot"

    def betRequest(self, game_state):
        game = GameState(game_state)
        player = game.our_player
        hole_cards = player.hole_cards
        community_cards = game.community_cards
        bet = player.bet
        stack = player.stack
        current_buy_in = game.current_buy_in
        minimum_raise = game.minimum_raise

        if hole_cards[0].rank == hole_cards[1].rank:
            # Pair
            if hole_cards[0].rank_value > 7:
                print("ALL IN:", json.dumps(hole_cards.__dict__))
                return 1000
            else:
                print("Don't go ALL IN:", json.dumps(hole_cards.__dict__))

        if hole_cards[0].rank_value > 9 or hole_cards[1].rank_value > 9:
            return current_buy_in - bet

        if current_buy_in > 200:
            return 0

        return current_buy_in - bet

    def showdown(self, game_state):
        pass
