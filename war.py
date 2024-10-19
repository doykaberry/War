#assignment of the card ranks and suits and face value ranks
J = 11
Q = 12
K = 13
A = 14
ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)
suits = ("hearts", "diamonds", "clubs", "spades")

#assignment of the full deck
deck = [(rank, suit) for rank in ranks for suit in suits]

#deck shuffling
import random
def shuffled_deck():
    random.shuffle(deck)
    return deck
shuffled = shuffled_deck()

#deck splitting and assignment of both player's decks
p1_deck = shuffled[0:26]
p2_deck = shuffled[26:]

#function to display the cards with face values
def display_card(card):
    rank, suit = card
    if rank == 11:
        rank_display = "J"
    elif rank == 12:
        rank_display = "Q"
    elif rank == 13:
        rank_display = "K"
    elif rank == 14:
        rank_display = "A"
    else:
        rank_display = rank
    return f"{rank_display} of {suit}"

#another war scenario
def anotherwar(p1_deck, p2_deck, p1_hand, p2_hand):
    ##prints the size of the deck so the user can see
    print(f"current deck size of p1: {len(p1_deck)}")
    print(f"current deck size of p2: {len(p2_deck)}")
    print("                                                                                                                     ")

    if len(p1_deck) < 4 or len(p2_deck) < 4:
        if len(p1_deck) < 4 and len(p2_deck) < 4: 
            print("Both players do not have enough cards to go to war. It's a stalemate!")
            exit() ##if both players cannot draw sufficient cards for a war it's a stalemate
        elif len(p1_deck) < 4:
            print("p1 does not have enough cards to fight in war!")
            print("                                                                                                                     ")
            print("p2 has won the game!")
            exit()
        elif len(p2_deck) < 4:
            print("p2 does not have enough cards to fight in war!")
            print("                                                                                                                     ")
            print("p1 has won the game!")
            exit()
    for card_p1 in range(4):
        p1_drawn_cards = p1_deck.pop(0)
        p1_hand.append(p1_drawn_cards) ##draws 4 cards from p1's deck
    print(f"p1's last drawn card is: {display_card(p1_hand[-1])}")
    for card_p2 in range(4):
        p2_drawn_cards = p2_deck.pop(0)
        p2_hand.append(p2_drawn_cards) ##draws 4 cards from p1's deck
    print(f"p2's last drawn card is: {display_card(p2_hand[-1])}")
    print("                                                                                                                     ")
    if int(p1_hand[-1][0]) > int(p2_hand[-1][0]):
        print("p1 has won this war") ##p1 wins if the fourth drawn card is greater than p2's fourth drawn card
        print("                                                                                                                     ")
        p1_deck.extend(p1_hand + p2_hand) ##puts both hands in p1's deck
    elif int(p2_hand[-1][0]) > int(p1_hand[-1][0]): ##p2 wins if the fourth drawn card is greater than p1's fourth drawn card
        print("p2 has won this war")
        print("                                                                                                                     ")
        p2_deck.extend(p2_hand + p1_hand) ##puts both hands in p2's deck
    else:
        print("Going to another war!")
        return anotherwar(p1_deck, p2_deck, p1_hand, p2_hand)
    return p1_deck, p2_deck

# war scenario
def war(p1_deck, p2_deck):
    if len(p1_deck) < 5:
        print("p1 does not have enough cards to fight in war!")
        print("                                                                                                                     ")
        print("p2 has won the game!")
        exit()
    if len(p2_deck) < 5:
        print("p2 does not have enough cards to fight in war!")
        print("                                                                                                                     ")
        print("p1 has won the game!")
        exit()
    ##assigning of p1's and p2's hands
    p1_hand = []
    p2_hand = []

    for card_p1 in range(5):
        p1_drawn_cards = p1_deck.pop(0)
        p1_hand.append(p1_drawn_cards) ##draws 5 cards from p1's deck which includes the original war card
    print(f"p1's last drawn card is: {display_card(p1_hand[-1])}")
    for card_p2 in range(5):
        p2_drawn_cards = p2_deck.pop(0)
        p2_hand.append(p2_drawn_cards) ##draws 4 cards from p2's deck which includes the original war card
    print(f"p2's last drawn card is: {display_card(p2_hand[-1])}")
    print("                                                                                                                     ")
    if int(p1_hand[4][0]) > int(p2_hand[4][0]):
        print("p1 has won this war")  ##p1 wins if the fifth drawn card is greater than p2's fifth drawn card
        print("                                                                                                                     ")
        p1_hand.extend(p2_hand)
        p1_deck.extend(p1_hand) ##puts both hands in p1's deck
    elif int(p2_hand[4][0]) > int(p1_hand[4][0]):
        print("p2 has won this war") ##p2 wins if the fifth drawn card is greater than p1's fifth drawn card
        print("                                                                                                                     ")
        p2_hand.extend(p1_hand)
        p2_deck.extend(p2_hand) ##puts both hands in p2's deck
    else:
        print("Another war is unravelling!") ##if the fifth card of both hands are equal, the anotherwar function is called
        print("                                                                                                                     ")
        p1_deck, p2_deck = anotherwar(p1_deck, p2_deck, p1_hand, p2_hand)
    return p1_deck, p2_deck

# playing a round
def play_round(p1_deck, p2_deck):
    while True: ##runs infinitley until the program is closed (when someone runs out of cards)
        print(f"current deck size of p1: {len(p1_deck)}")
        print(f"current deck size of p2: {len(p2_deck)}")
        print("                                                                                                                     ")
        if len(p1_deck) == 0:
            print("p1 has no more cards to play a round!")
            print("                                                                                                                     ")
            print("p2 has won the game")
            exit()
        elif len(p2_deck) == 0:
            print("p2 has no more cards to play a round!")
            print("                                                                                                                     ")
            print("p1 has won the game")
            exit()
        else:    
            p1_card = p1_deck.pop(0)
            p2_card = p2_deck.pop(0) ##takes a card from each deck
            print(f"p1's card is: {display_card(p1_card)}")
            print(f"p2's card is: {display_card(p2_card)}")
            print("                                                                                                                     ")
            ##comparing of cards
            if p1_card[0] > p2_card[0]: 
                print("p1 has won this round")
                print("                                                                                                                     ")
                p1_deck.append(p1_card)
                p1_deck.append(p2_card) ##adds the cards to the end of the deck of the winner

            elif p1_card[0] < p2_card[0]:                   
                print("p2 has won this round")
                print("                                                                                                                     ")
                p2_deck.append(p2_card)
                p2_deck.append(p1_card) ##adds the cards to the end of the deck of the winner
            else: ##this else block runs if both cards are equal to each other
                print("A war is set to unfold")
                print("                                                                                                                     ")
                p1_deck.insert(0, p1_card)
                p2_deck.insert(0, p2_card) ## puts both player's "war" card back into the deck (this is done for simplification purposes)
                p1_deck, p2_deck = war(p1_deck, p2_deck)

# running the game
def play_game():
    print("Welcome to the game of Peace!")
    play_round(p1_deck, p2_deck) ##plays rounds until someone either wins, loses, or ties

play_game() ##runs the game
