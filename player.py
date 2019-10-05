import json
import sys

from game import GameState

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]


class Player:
    VERSION = "Rampage bot"

    def betRequest(self, game_state):
        game = GameState(game_state)
        player = game.our_player
        hole_cards = player.hole_cards
        community_cards = game.community_cards
        bet = player.bet
        stack = player.stack
        current_buy_in = game.community_cards
        minimum_raise = game.minimum_raise

        if hole_cards[0]['rank'] == hole_cards[1]['rank']:
            rank = 14 - RANKS[-1::-1].index(hole_cards[0]['rank'])
            # Pair
            if rank > 7:
                print("ALL IN:", json.dumps(hole_cards))
                return 1000
            else:
                print("Don't go ALL IN:", json.dumps(hole_cards))

        if current_buy_in > 200:
            return 0

        return current_buy_in - bet

    def showdown(self, game_state):
        pass
