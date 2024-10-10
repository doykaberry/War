def compare_cards(p1_card, p2_card):
    #takes two cards and returns an int representing who has the stronger card

def gameloop():
    #move the turns along it determines when the game is done

    while len(p1_deck) == 0 and len(p2_deck) > 0:
        #this is where you put the logic for one turn
        # p1_deck.pop(0) removes card from deck
        #3 functions u will need list.append(x): add to end of list
        #list.pop(0) removes and returns item at index 0 from the list
        #list.index(x) finds the index x in the list. could error if x is not in the list
        #p1_card = p1_deck.pop(0)
        p1card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)
        result ==1: # player 1 has won
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
    if len(p1_deck)>0:
        print("p1 won")
    else:
        print("p2 won")


#start of program

#assignment of the card ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

#assignment of the full deck
deck = [(rank, suit) for rank in ranks for suit in suits]

#deck shuffling
import random
def shuffled_deck():
    random.shuffle(deck)
    return deck
    
#deck splitting and assignment of both player's decks
p1_deck = shuffled_deck()[0:26]
p2_deck = shuffled_deck()[26:]

#assignment of card in both player's hands
def p1_card():
    for card_p1 in range(len(p1_deck)):
       p1_deck.pop(card_p1)

p12_card = p1_deck.pop()
p2_card = p2_deck.pop()












