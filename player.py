import json

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]


class Player:
    VERSION = "Rampage bot"

    def betRequest(self, game_state):
        # game = GameState(game_state)
        # player = game.our_player
        # hole_cards = player.hole_cards
        # community_cards = game.community_cards
        # bet = player.bet
        # stack = player.stack
        # current_buy_in = game.current_buy_in
        # minimum_raise = game.minimum_raise

        player = game_state['players'][game_state['in_action']]
        hole_cards = player['hole_cards']
        # community_cards = game_state['community_cards']
        bet = player['bet']
        stack = player['stack']
        current_buy_in = game_state['current_buy_in']
        minimum_raise = game_state['minimum_raise']

        if hole_cards[0]['rank'] == hole_cards[1]['rank']:
            rank = 14 - RANKS[-1::-1].index(hole_cards[0]['rank'])
            if rank > 7:
                print("ALL IN:", json.dumps(hole_cards))
                return 1000
            else:
                print("Don't go ALL IN:", json.dumps(hole_cards))

        # if hole_cards[0].rank_value > 9 or hole_cards[1].rank_value > 9:
        #     print("response:", current_buy_in - bet)
        #     return current_buy_in - bet

        if current_buy_in > 200:
            return 0

        print("response:", current_buy_in - bet)
        return current_buy_in - bet

    def showdown(self, game_state):
        pass
