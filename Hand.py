from enum import Enum

from Card import orderCardsByRank


class HandRank(Enum):
	HIGHCARD = 1
	PAIR = 2
	TWO_PAIR = 3
	THREE_OF_A_KIND = 4
	STRAIGHT = 5
	FLUSH = 6
	FULLHOUSE = 7
	POKER = 8
	STRAIGHT_FLUSH = 9

def GetHandRank(CardList):
	hand = HandRank.HIGHCARD
	CardList.sort(key=orderCardsByRank)
	Ranks = []
	for i in range(2, 14):
		Ranks.append(0)
	for card in CardList:
		Ranks[card.Rank-2] += 1
	max = 0
	Ranks.sort(reverse = True)
	if Ranks[0] == 4:
		return HandRank.POKER
	if Ranks[0] == 3:
		if Ranks[1] >= 2:
			return HandRank.FULLHOUSE
		else:
			return HandRank.THREE_OF_A_KIND
	if Ranks[0] == 2:
		if Ranks[1] == 2:
			return HandRank.TWO_PAIR
		else:
			return HandRank.PAIR


class Hand:
	cards = []
	#def best 
