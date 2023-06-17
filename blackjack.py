from random import choice

hand_list = [["A", 1], ["2", 2], ["3", 3], ["4", 4], ["5", 5], ["6", 6], [
    "7", 7], ["8", 8], ["9", 9], ["10", 10], ["J", 10], ["Q", 10], ["K", 10]]

dealer_hand = []
player_hand = []
first_dealer_card = choice(hand_list)
second_dealer_card = choice(hand_list)
dealer_hand.append(first_dealer_card[0])
dealer_hand.append(second_dealer_card[0])
value_dealer_hand = first_dealer_card[1]
print(
    f"\nDealer Hand is [{first_dealer_card[0]},X] and the value of the hand is {value_dealer_hand}\n")

player_hand_1 = choice(hand_list)
player_hand_2 = choice(hand_list)
player_hand.append(player_hand_1[0])
player_hand.append(player_hand_2[0])
value_player_hand = player_hand_1[1] + player_hand_2[1]
if (player_hand_1[0] == "A" or player_hand_2[0] == "A") and value_player_hand < 12:
    value_player_hand += 10

print(
    f"\nPlayer Hand is {player_hand} and the value of the hand is {value_player_hand}\n")

choice_inside = int(input("""
        Do you want to
        1. Hit
        2. Stand
        """))

while choice_inside == 1:
    player_hand_n = choice(hand_list)
    player_hand.append(player_hand_n[0])
    value_player_hand += player_hand_n[1]
    print(
        f"\nPlayer Hand is {player_hand} and the value of the hand is {value_player_hand}\n")

    if value_player_hand > 21:
        print("Bust!! You have lost! Dealer Wins!!!!!")
        break
    elif value_player_hand == 21:
        print("Blackjack! You win!")
        break

    choice_inside = int(input("""
        Do you want to
        1. Hit
        2. Stand
        """))

if choice_inside == 2:
    value_dealer_hand += second_dealer_card[1]
    if (first_dealer_card[0] == "A" or second_dealer_card[0] == "A") and value_dealer_hand < 12:
        value_dealer_hand += 10

    print(
        f"\nDealer Hand is {dealer_hand} and the value of the hand is {value_dealer_hand}\n")

    while value_dealer_hand < 17:
        dealer_hand_n = choice(hand_list)
        dealer_hand.append(dealer_hand_n[0])
        value_dealer_hand += dealer_hand_n[1]
        print(
            f"\nDealer Hand is {dealer_hand} and the value of the hand is {value_dealer_hand}\n")

    if value_dealer_hand > 21:
        print(
            f"Player Hand is {player_hand} Value is {value_player_hand} and Dealer hand is {dealer_hand} the value of the dealer hand is {value_dealer_hand} \n\nDealer busts! You win!")
    elif value_dealer_hand > value_player_hand:
        print(
            f"Player Hand is {player_hand} Value is {value_player_hand} and Dealer hand is {dealer_hand} the value of the dealer hand is {value_dealer_hand} \n\nDealer Wins!")
    elif value_dealer_hand < value_player_hand:
        print(
            f"Player Hand is {player_hand} Value is {value_player_hand} and Dealer hand is {dealer_hand} the value of the dealer hand is {value_dealer_hand} \n\nYou win!")
    else:
        print(
            f"Player Hand is {player_hand} Value is {value_player_hand} and Dealer hand is {dealer_hand} the value of the dealer hand is {value_dealer_hand} \n\nIt's a Tie!")
