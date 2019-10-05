import json

from game import GameState
from logger import Logger
from preflop import Preflop

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]


class Player:
    VERSION = "Chennin' bot"

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

        if len(community_cards) == 0:
            try:
                score = Preflop(game_state).score()

                if score > 10:
                    logger.all_in("Chen said it's fine")
                    return 4000

                if score < 6:
                    logger.all_in("Chen score is low")
                    return 0

                logger.check("Chen says we should check")
                return current_buy_in - bet
            except:
                print('WTF?')
                pass

        if hole_cards[0].rank == hole_cards[1].rank:
            if hole_cards[0].rank_value > 7:
                logger.all_in("high cards")
                return 1000

        if hole_cards[0].rank_value > 9 or hole_cards[1].rank_value > 9:
            if current_buy_in > 500 and bet < 200:
                logger.fold("high card, high stakes, low money")
                return 0

            logger.check("at least one high card")
            return current_buy_in - bet

        if current_buy_in > 350 and bet < 80:
            logger.fold("high stakes, low money")
            return 0

        logger.check("no reason to stop now")
        return current_buy_in - bet

    def showdown(self, game_state):
        pass
