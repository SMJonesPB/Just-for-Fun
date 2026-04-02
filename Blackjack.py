import random

# Card values: Ace can be 1 or 11
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def create_deck():
    """Create and return a shuffled deck of 52 cards."""
    suits = ['♠', '♥', '♦', '♣']
    ranks = list(CARD_VALUES.keys())
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    """Calculate the best value for a hand considering Aces."""
    value = sum(CARD_VALUES[card[:-1]] for card in hand)
    aces = sum(1 for card in hand if card.startswith('A'))
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

def display_hand(name, hand, hide_first=False):
    """Display a player's or dealer's hand."""
    if hide_first:
        print(f"{name}'s hand: [Hidden], {hand[1]}")

    else:
        print(f"{name}'s hand: {', '.join(hand)} (Value: {calculate_hand_value(hand)})")

def player_turn(deck, hand, chips, bet):
    """Handle a single player's turn."""
    while True:
        if calculate_hand_value(hand) == 21:
            print("Blackjack!")
            break

        choice = input("[H]it, [S]tand, [D]ouble down: ").strip().lower()
        if choice not in ['h', 's', 'd']:
            print("Invalid choice.")
            continue

        if choice == 'h':
            hand.append(deck.pop())
            display_hand("Player", hand)
            if calculate_hand_value(hand) > 21:
                print("Busted!")
                return False, bet
            
        elif choice == 'd':
            if chips >= bet:
                bet *= 2
                hand.append(deck.pop())
                display_hand("Player", hand)
                if calculate_hand_value(hand) > 21:
                    print("Busted!")
                    return False, bet
                
                break
            else:
                print("Not enough chips to double down.")
                continue

        else:
            break

    return True, bet

def dealer_turn(deck, hand):
    """Dealer hits until reaching at least 17."""
    while calculate_hand_value(hand) < 17:
        hand.append(deck.pop())

    return calculate_hand_value(hand) <= 21

def play_blackjack():
    """Main game loop with multiple players and splitting."""
    num_players = 0
    while num_players < 1 or num_players > 4:
        try:
            num_players = int(input("Enter number of players (1-4): "))

        except ValueError:
            print("Enter a valid number.")

    chips = [500] * num_players  # Each player starts with 500 chips

    print("\n=== Welcome to Multiplayer Casino Blackjack ===")
    while any(c > 0 for c in chips):
        deck = create_deck()
        bets = []
        player_hands = [[] for _ in range(num_players)]
        dealer_hand = [deck.pop(), deck.pop()]

        # Place bets
        for i in range(num_players):
            if chips[i] <= 0:
                bets.append(0)
                continue

            while True:
                try:
                    bet = int(input(f"Player {i+1} ({chips[i]} chips), place your bet: "))
                    if 0 < bet <= chips[i]:
                        bets.append(bet)
                        break
                    else:
                        print("Invalid bet amount.")
                except ValueError:
                    print("Enter a valid number.")

        # Deal initial cards
        for i in range(num_players):
            if bets[i] > 0:
                player_hands[i] = [deck.pop(), deck.pop()]

        display_hand("Dealer", dealer_hand, hide_first=True)

        # Player turns
        for i in range(num_players):
            if bets[i] == 0:
                continue

            print(f"\n--- Player {i+1}'s turn ---")
            display_hand(f"Player {i+1}", player_hands[i])

            # Splitting option
            if (player_hands[i][0][:-1] == player_hands[i][1][:-1] and
                chips[i] >= bets[i]):
                split_choice = input("Do you want to split? (y/n): ").strip().lower()
                if split_choice == 'y':
                    second_hand = [player_hands[i].pop()]
                    player_hands[i].append(deck.pop())
                    second_hand.append(deck.pop())
                    print("First hand:")
                    alive1, bet1 = player_turn(deck, player_hands[i], chips[i], bets[i])
                    print("Second hand:")
                    alive2, bet2 = player_turn(deck, second_hand, chips[i], bets[i])
                    player_hands[i] = [(player_hands[i], alive1, bet1),
                                       (second_hand, alive2, bet2)]
                    
                    continue

            alive, bets[i] = player_turn(deck, player_hands[i], chips[i], bets[i])
            player_hands[i] = [(player_hands[i], alive, bets[i])]

        # Dealer's turn
        print("\nDealer's turn:")
        display_hand("Dealer", dealer_hand)
        dealer_alive = dealer_turn(deck, dealer_hand)
        display_hand("Dealer", dealer_hand)

        dealer_value = calculate_hand_value(dealer_hand)

        # Determine results
        for i in range(num_players):
            if bets[i] == 0:
                continue

            for hand, alive, bet in player_hands[i]:
                if not alive:
                    chips[i] -= bet

                else:
                    player_value = calculate_hand_value(hand)

                    if not dealer_alive or player_value > dealer_value:
                        print(f"Player {i+1} wins {bet} chips!")
                        chips[i] += bet

                    elif player_value < dealer_value:
                        print(f"Player {i+1} loses {bet} chips.")
                        chips[i] -= bet
                        
                    else:
                        print(f"Player {i+1} pushes (tie).")

        # Check if players want to continue
        cont = input("\nPlay another round? (y/n): ").strip().lower()
        if cont != 'y':
            break

    print("\n=== Final Chip Counts ===")
    for i in range(num_players):
        print(f"Player {i+1}: {chips[i]} chips")

if __name__ == "__main__":
    play_blackjack()
