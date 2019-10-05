from enum import Enum

class Suits(Enum):
	spade = 1
	heart = 2
	diamond = 3
	club = 4

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
	Suits
	Rank

def orderCardsByRank (x, y):
	return x.Rank > y.Rank