import json

import sys

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]

class Player:
    VERSION = "Much better all in bot"

    def betRequest(self, game_state):
        print("Python version:", sys.version)
        player = game_state['players'][game_state['in_action']]
        hole_cards = player['hole_cards']
        community_cards = game_state['community_cards']
        bet = player['bet']
        stack = player['stack']
        current_buy_in = game_state['current_buy_in']
        minimum_raise = game_state['minimum_raise']

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
