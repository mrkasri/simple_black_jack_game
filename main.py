############### Blackjack Project #####################


############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
import logo
import os




def deal_card():
  """ Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
def calculate_score(cards):
    """Take a list of cards and return their score"""
    if sum(cards)==21 and len(cards)==2:
        return 0

    if sum(cards) > 21 and 11 in cards :
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
def compare(user_score ,computer_score):
    if user_score ==computer_score:
        print('Draw')
    elif user_score==0:
        print('You win, you have Blackjack')
    elif computer_score==0:
        print('Computer wins, it has Blackjack')
    elif user_score > 21:
        print('Computer wins, you went over')
    elif computer_score > 21:
        print('You win, computer went over')
    elif user_score > computer_score:
        print('You win')
    else:
        print('Computer wins')

def play_blackjack():
    print(logo.logo)
    user_cards = []
    computer_cards = []
    is_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())



    while not is_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'Your cards:{user_cards}, and your score:{user_score}')
        print(f'Computer\'s first card:{computer_cards[0]}')

        if computer_score==0 or user_score==0 or user_score > 21:
            is_over=True
            print('The game ended.')
        else:
            if input('Do you want to draw another card? yes or no:')=='yes':
                user_cards.append(deal_card())
            else:
                is_over=True
                print('The game ended.')


    while computer_score < 17 and computer_score!=0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Your final hand:{user_cards}, final score:{user_score}')
    print(f'Computer\'s  final hand:{computer_cards}, final score:{computer_score}')
    compare(user_score,computer_score)

play_blackjack()
while input('Do you want to play again ? yes or no:')=='yes':
    os.system('clear')
    play_blackjack()
