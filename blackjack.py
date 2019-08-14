import random


# def get_hand(player, hand):
#     return 'Your hand is : ' + hand

def check_player_bust(player_hand):
    player_value = 0
    for x in player_hand:
        player_value += cards[x]
    if player_value > 21: 
        return True
    else: 
        return False

def check_dealer_bust(dealer_hand):
    dealer_value = 0
    for x in dealer_hand:
        dealer_value +=  cards[x]
    if dealer_value > 21: 
        return True
    else: 
        return False

def get_player_hand_sum(hand):
    value = 0
    for x in hand:
        value += cards[x]
    print(f"Player's current hand value is {value}")

def get_dealer_hand_sum(hand):
    value = 0
    for x in hand:
        value += cards[x]
    print(f"Dealer's current hand value is {value}")

def get_hand_sum(hand):
    value = 0
    for x in hand:
        value += cards[x]
    return value


def deal_card(hand):
    hand.append(random.choice(list(cards.keys())))
    return hand

def deal_two_cards(player_hand, dealer_hand):       
        randomCardChoice1 = random.choice(list(cards.keys()))
        randomCardChoice2 = random.choice(list(cards.keys()))
        player_hand.append(randomCardChoice1)
        player_hand.append(randomCardChoice2)

        randomCardChoice1 = random.choice(list(cards.keys()))
        randomCardChoice2 = random.choice(list(cards.keys()))
        dealer_hand.append(randomCardChoice1)
        dealer_hand.append(randomCardChoice2)
        return player_hand, dealer_hand

def check_21(player_hand, dealer_hand):
    if get_hand_sum(dealer_hand) == 21:
        return '21 Dealer Wins'

    elif get_hand_sum(player_hand) == 21: 
        return '21 Player Wins'
    else:
         return "NA"

def check_win(player_hand,dealer_hand):
    if (get_hand_sum(dealer_hand) > get_hand_sum(player_hand)) and (get_hand_sum(dealer_hand) <= 21):
        return "Dealer Wins"

    elif get_hand_sum(dealer_hand) < get_hand_sum(player_hand) and (get_hand_sum(player_hand ) <= 21):
        return "Player Wins"
    else: 
        return "NA"

  


def play_blackjack():
    player_hand = []
    dealer_hand = []
    play = True
    print('Welcome to BlackJack!'+ '\n')
    
    cards ={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

    # Load two cards to both hands 
    player_hand, dealer_hand = deal_two_cards(player_hand,dealer_hand)    
    
    while play:
        # Check if player Busted
        if check_player_bust(player_hand):
            play = False
            return print('Player Busted!! Dealer Wins!')
        
        # Check if dealer busted
        if check_dealer_bust(dealer_hand):
            play = False
            return print('Dealer Busted!! Player Wins!')

        print(f'Dealer, your visible cards is {dealer_hand}')
        print(f'Player, your cards are {player_hand}')
        get_dealer_hand_sum(dealer_hand)
        get_player_hand_sum(player_hand)
        
        

        choice = input("Player do you want to stay or hit? ")

        if choice.lower() == 'stay':
            while (get_hand_sum(dealer_hand) <= 17):

                deal_card(dealer_hand)

                twenty_one = check_21(player_hand, dealer_hand)

                if twenty_one != 'NA':
                    return twenty_one

                get_dealer_hand_sum(dealer_hand)

                if (check_dealer_bust(dealer_hand)):
                    print('Dealer Busted! Player wins.')
                    play = False

            win = check_win(player_hand, dealer_hand)

            if (win != 'NA'):
                return win 


        elif choice.lower() == 'hit':
            deal_card(player_hand)

            get_player_hand_sum(player_hand)

            twenty_one = check_21(player_hand, dealer_hand)

            if twenty_one != 'NA':
                return twenty_one

            if (check_player_bust(player_hand)):
                    print('Player Busted! Dealer wins.')
                    get_player_hand_sum(player_hand)
                    play = False




        
    




                                  
