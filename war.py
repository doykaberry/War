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
