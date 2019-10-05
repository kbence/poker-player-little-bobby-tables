from enum import Enum

class Suits(Enum):
	SPADE = 1
	HEART = 2
	DIAMOND = 3
	CLUB = 4

class Rank(Enum):
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13
	ACE = 14



class Card:
	suit
	rank
	def __init__ ():
		return

def getCardFromJson (JsonObj):
	x = Card()
	jsuit = JsonObj["suit"]
	if (jsuit == "spades"):
		x.suit = Suits.SPADE
	if (jsuit == "hearts"):
		x.suit = Suits.HEART
	if (jsuit == "diamonds"):
		x.suit = Suits.DIAMOND
	if (jsuit == "clubs"):
		x.suit = Suits.CLUB
	jrank = JsonObj["rank"]
	if ( jrank == "A" ):
		x.rank = Rank.ACE
	elif ( jrank == "K" ):
		x.rank = Rank.KING
	elif ( jrank == "Q" ):
		x.rank = Rank.QUEEN
	elif ( jrank == "J" ):
		x.rank = Rank.JACK
	else:
		x.rank = Rank(int(jrank))
	return x



def orderCardsByRank (x, y):
	return x.Rank > y.Rank