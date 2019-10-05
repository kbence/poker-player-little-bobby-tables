from Card import orderCardsByRank

class HandRank:
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
    for i in range(2, 15):
        Ranks.append(0)
    for card in CardList:
        Ranks[card.Rank-2] += 1
    if len(CardList) >= 5: # check for straight
        con = 0 # continous cards amount
        lastRank = 0
        for i in range(2,15):
            if lastRank == 0 and Ranks[i-2] != 0:
                lastRank = i
                con = 1
            elif lastRank+1 == i:
                lastRank += 1
                con += 1
            else:
                con = 0
            if con == 5:
                hand = HandRank.STRAIGHT
    max = 0
    Ranks.sort(reverse = True)
    if len(CardList) >= 5: #check for flush
        suitList = {0,0,0,0}
        for card in CardList:
            suitList[int(card.suit)] += 1
        for i in range(0,4):
            if i >= 5:
                if hand == HandRank.STRAIGHT:
                    return HandRank.STRAIGHT_FLUSH # todo check for royal?
                else:
                    hand = HandRank.FLUSH
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

def PreFlop (CardsInHand):
    return 1000 # todo

def Flop (CardsInHand, TableCards):
    return PreFlop(CardsInHand) # todo

def Turn  (CardsInHand, TableCards):
    return Flop(CardsInHand,TableCards) # todo

def River (CardsInHand, TableCards):
    return Turn(CardsInHand, TableCards) # todo
class Hand:
    cards = []

    
