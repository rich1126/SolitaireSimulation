## The rules of this Solitaire game is that you draw a single card at a time
## You only look at the most recent four cards in your hand
## If the "first" and "fourth" cards you're looking at are the same suit,
## discard the two cards in between them ("third" and "second")

## This is a simulation to look at the distribution of cards withdrawn in a game

import random


def draw(hand, deck, n):
    hand.append(deck[n])
    return hand

def simulation(Deck):
    random.shuffle(Deck)
    hand = []  ## Current set of cards drawn

    n = 0 ## To keep track of order in deck

    while n < 52:
        while len(hand) < 4:
            if n < 52:
                hand = draw(hand, Deck, n)
                n += 1
        
        while hand[-1] == hand[-4]:
             del hand[-2]
             del hand[-2]
             if len(hand) < 4:
                 break
        if n < 52:
            hand = draw(hand, Deck, n)
            n += 1
    
    return len(hand)

def main():
    ##The numbers are irrelevant to the game, so we create a deck that consists of 13 of each suit

    unshuffledDeck = ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", 
    "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", 
    "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", 
    "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]
    n = 10000
    dataFile = open('simResults.txt', 'w')
    for i in range(n):
        result = simulation(unshuffledDeck)
        dataFile.write(str(result))
        dataFile.write('\n')
    
    dataFile.close()

if __name__ == '__main__':
    main()
