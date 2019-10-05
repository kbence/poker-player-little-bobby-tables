
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        player = game_state['players'][game_state['in_action']]
        hole_cards = player['hole_cards']
        community_cards = game_state['community_cards']
        bet = player['bet']
        stack = player['stack']
        current_buy_in = game_state['current_buy_in']
        minimum_raise = game_state['minimum_raise']

        if hole_cards[0]['rank'] == hole_cards[1]['rank']:
            # Pair
            return 1000

        return current_buy_in - bet

    def showdown(self, game_state):
        pass
