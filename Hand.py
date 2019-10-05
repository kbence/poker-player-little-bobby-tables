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
	CardList.sort(key=orderCardsByRank)
	Ranks = []
	for i in range(2, 5):
		Ranks.append(0)
	for card in CardList:
		Ranks[card.Rank-2] += 1

class Hand:
	cards = []
	#def best 
