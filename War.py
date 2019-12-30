## This is a card game played with a standard deck of 52 cards fo two players

import random

class Card:
    
    # a list of 14 ranks; a list of 4 suits
    cardRank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    cardSuit = ["C","D","H","S"]

    # create two variables rank and suit for Card
    def __init__(self,rank,suit):
            self.rank = rank
            self.suit = suit

    # print an individual card(3 spaces each)
    def __str__(self):   
        # formatting the output of card 
        outStr = format((self.rank + self.suit), ">4s")
        return outStr
    
    # a function for converting letters in rank into numbers (for comparison)
    def convert(self):
        if self.rank == "J":
            cardRank = 11
        elif self.rank == "Q":
            cardRank = 12
        elif self.rank == "K":
            cardRank = 13
        elif self.rank == "A":
            cardRank = 14
        else:
            cardRank = int(self.rank)
      
        return cardRank
        

class Deck:

    # create the variable cardList, which includes are 52 cards
    def __init__(self):
        self.cardList = []
        for suit in Card.cardSuit:
            for rank in Card.cardRank:
                card = Card(rank,suit)
                self.cardList.append(card)

    # rearrange the elements of the list myList into a random order
    def shuffle(self):
        random.shuffle(self.cardList)

    # remove the first card from the deck's cardList
    def dealOne(self,player):

        # remove the 1st card from the list
        newCard = self.cardList.pop(0)
        # add it to a player's card list.
        player.hand.append(newCard)
        player.handTotal = len(player.hand)
        

    # print out the cardList of all 52 cards in 4 rows of 13 cards.
    def __str__(self):
        outStr = ""
        counter = 0   # for formatting

        for i in range(len(self.cardList)):
            outStr += str(self.cardList[i])
            counter += 1
            
            # The index of card is a multiple of 13, then go to the next row
            if counter % 13 == 0:
                outStr += "\n"

        return outStr


class Player:

    # set hand to an empty list and handTotal to zero
    def __init__(self):
        self.hand = []
        self.handTotal = 0
        
    # print out the hand of a player
    def __str__(self):
        outStr = ""
        counter = 0
        
        for i in range(len(self.hand)):
            outStr += str(self.hand[i])
            counter += 1
            
            # The index of card is a multiple of 13, then go to the next row
            if counter % 13 == 0:
                outStr += "\n"

        return outStr

    # check if a player has any cards
    def handNotEmpty(self):
        return self.hand != []
        

# how the game really runs with appropriate descriptions
def playGame(deck,player1,player2):

    # print out what two players have in hand at beginning
    print ("\n\nInitial hands: ")
    print ("Player 1:   ")
    print (player1)
    print ("\nPlayer 2:")
    print (player2)
    
    # create a variable to count rounds
    count = 0
    
    # make sure they also have cards in hand
    while player1.handNotEmpty() and player2.handNotEmpty():
        # print out which round it is and each player's card
        count += 1
        print("\n\nROUND " + str(count) + ":")
        
        # call the compare function  
        compare(player1,player2,[],[],count)

        # print out what two players have in hand when a round completed
        print("Player 1 now has", len(player1.hand),"card(s) in hand:")
        print(player1)
        print("Player 2 now has", len(player2.hand),"card(s) in hand:")
        print(player2)

    
       
# pop and add cards, compare the value of two cards using recursion
# create two lists to store played cards: playedCard1 and playedCard2
def compare(player1,player2,playedCard1,playedCard2,count):
    
    # stop the game when either of the players has no card
    if len(player1.hand) == 0 or len(player2.hand) == 0:
        return

    card1 = player1.hand.pop(0)        # player 1 plays a card
    card2 = player2.hand.pop(0)        # player 2 plays a card
    playedCard1.append(card1)
    playedCard2.append(card2)

    print("Player 1 plays:" + str(card1))
    print("Player 2 plays:" + str(card2), "\n")
    
    # when player1's card > player2's card
    if card1.convert() > card2.convert():
        print("Player 1 wins round " + str(count) + ":" + str(card1) + " >" \
              + str(card2) + "\n")
        player1.hand.extend(playedCard1)
        player1.hand.extend(playedCard2)
        return
    
    # when player2's card > player1's card
    elif card1.convert() < card2.convert():
        print("Player 2 wins round " + str(count) + ":" + str(card2) + " >" \
              + str(card1) + "\n")
        player2.hand.extend(playedCard1)
        player2.hand.extend(playedCard2)
        return

    # when player1's card = player2's card
    else:
        print("War starts:" + str(card1) + " =" + str(card2))
        
        # each player draws three additional cards
        for i in range(3):
            card1 = player1.hand.pop(0)
            card2 = player2.hand.pop(0)
            playedCard1.append(card1)
            playedCard2.append(card2)
            print("Player 1 puts" + str(card1) + " face down")
            print("Player 2 puts" + str(card2) + " face down")

        # recognize which card they are gonna play next
        cardFight1 = player1.hand[0]
        cardFight2 = player2.hand[0]
        print("Player 1 puts" + str(cardFight1) + " face up")
        print("Player 2 puts" + str(cardFight2) + " face up")

        # use recursion to call this function itself to make camparison again
        compare(player1,player2,playedCard1,playedCard2,count)
        

        
def main():

    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    player1 = Player()              # create a player
    player2 = Player()              # create another player

    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)
    
    playGame(cardDeck,player1,player2)

    if player1.handNotEmpty():
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")

    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    print (player1)                 # printing a player object should print that player's hand
    print ("\nPlayer 2:")
    print (player2)                 # one of these players will have all of the cards, the other none
    
main()
