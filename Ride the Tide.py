import random

CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}


def create_deck():
    """Create and return a shuffled deck of 52 cards."""
    suits = ['♠', '♥', '♦', '♣']
    ranks = list(CARD_VALUES.keys())
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


def card_value(card):
    """Return numeric value of a card like '10♠' or 'K♥'."""
    rank = card[:-1]  # everything except the suit
    return CARD_VALUES[rank]


def draw_card(deck):
    """Draw the top card from the deck."""
    return deck.pop()


def dealer_choice(last_value):
    """
    Simple dealer strategy:
    - 2–6  -> guess higher
    - 10–A -> guess lower
    - 7–9  -> stand
    """
    if 2 <= last_value <= 6:
        return "h"
    
    elif 10 <= last_value <= 14:
        return "l"
    
    else:
        return "S"


def take_turn(player_name, hand, deck, is_dealer=False):
    """
    Run a full turn for a player or dealer.
    Returns the final hand (cleared to [] if you guess wrong).
    """
    # First card
    hand.append(draw_card(deck))
    print("_____________________________________________________________________")
    print(f"{player_name}'s turn")

    while True:
        print(f"\n{player_name}'s hand: {hand}")
        print(f"Last card: {hand[-1]}")
        last_card = hand[-1]
        last_value = card_value(last_card)

        if is_dealer:
            choice = dealer_choice(last_value)
            if choice == "h":
                print("The dealer guesses higher.")
            elif choice == "l":
                print("The dealer guesses lower.")

            
            else:
                print("The dealer stands.")
        else:
            raw = input("Do you want to guess higher, lower, or stand? (h/l/s) ").strip().lower()
            if not raw:
                choice = "s"
            else:
                choice = raw[0]  # "h", "l", or "s"

        if choice == "s":
            break

        # Draw new card and compare
        new_card = draw_card(deck)
        hand.append(new_card)
        print(f"New card: {new_card}")
        new_value = card_value(new_card)

        correct = (
            (choice == 'h' and new_value >= last_value) or
            (choice == 'l' and new_value <= last_value)
        )

        if correct:
            print("Correct!")
            if len(hand) == 6:
                # Reached 6 cards: ride the tide
                break
        else:
            print("Wrong.")
            # A wrong guess means you lose all progress
            hand.clear()
            break

    return hand


def summarize_results(players, dealer):
    dealer_guesses = len(dealer["hand"])
    print("\n================= RESULTS =================")
    print(f"Dealer's correct guesses: {dealer_guesses}")

    all_zero = dealer_guesses == 0 and all(len(p["hand"]) == 0 for p in players)
    if all_zero:
        print("Everyone guessed wrong.")

    for p in players:
        guesses = len(p["hand"])
        name = p["name"]
        print(f"\n{name}'s correct guesses: {guesses}")

        if guesses == 6:
            print(f"{name} rides the tide!")
            continue

        if guesses == 0:
            print(f"{name} guessed wrong.")
            continue

        if dealer_guesses == 0:
            print(f"The dealer guessed wrong. {name} wins!")
        else:
            if guesses > dealer_guesses:
                print(f"{name} wins!")
            elif guesses == dealer_guesses:
                print(f"{name} ties.")
            else:
                print(f"{name} loses.")


def get_number_of_players():
    while True:
        n = input("How many players are there from 1 to 3 (excluding the dealer)? ").strip()
        if n in {"1", "2", "3"}:
            return int(n)
        
        print("You must type a number from 1 to 3.")


def play_ride_the_tide():
    deck = create_deck()
    num_players = get_number_of_players()

    players = [{"name": f"Player {i+1}", "hand": []} for i in range(num_players)]
    dealer = {"name": "Dealer", "hand": []}

    # Players take turns
    for p in players:
        take_turn(p["name"], p["hand"], deck, is_dealer=False)

    # Dealer's turn
    take_turn(dealer["name"], dealer["hand"], deck, is_dealer=True)

    # Results
    summarize_results(players, dealer)


if __name__ == "__main__":
    play_ride_the_tide()