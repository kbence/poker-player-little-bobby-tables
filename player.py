import json

from game import GameState
from logger import Logger

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]


class Player:
    VERSION = "Rampage bot"

    def betRequest(self, game_state):
        game = GameState(game_state)
        logger = Logger(game)
        player = game.our_player
        hole_cards = player.hole_cards
        community_cards = game.community_cards
        bet = player.bet
        stack = player.stack
        current_buy_in = game.current_buy_in
        minimum_raise = game.minimum_raise

        if hole_cards[0].rank == hole_cards[1].rank:
            rank = 14 - RANKS[-1::-1].index(hole_cards[0].rank)
            if rank > 7:
                logger.all_in("high cards")
                return 1000

        if hole_cards[0].rank_value > 9 or hole_cards[1].rank_value > 9:
            logger.check("at least one high card")
            return current_buy_in - bet

        if current_buy_in > 350 and bet < 80:
            logger.fold("high stakes, low money")
            return 0

        logger.check("no reason to stop now")
        return current_buy_in - bet

    def showdown(self, game_state):
        pass
