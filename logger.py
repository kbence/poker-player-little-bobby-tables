

class Logger:
    def __init__(self, state):
        self._state = state

    def act(self, what, why):
        print '{} "{}" hole={}, community={} game_id={}'.format(
            what, why,
            self._state.our_player.hole_cards,
            self._state.community_cards,
            self._state.game_id,
        )

    def fold(self, reason):
        self.act('fold', reason)

    def all_in(self, reason):
        self.act('all_in', reason)

    def check(self, reason):
        self.act('check', reason)
