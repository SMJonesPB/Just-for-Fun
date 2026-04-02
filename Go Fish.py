import random

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

    def __len__(self):
        return len(self.cards)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.books = []

    def draw_card(self, deck):
        card = deck.draw()
        if card:
            self.hand.append(card)
        return card

    def has_rank(self, rank):
        return any(card.rank == rank for card in self.hand)

    def give_all_rank(self, rank):
        matching = [card for card in self.hand if card.rank == rank]
        self.hand = [card for card in self.hand if card.rank != rank]
        return matching

    def check_for_books(self):
        rank_counts = {}
        for card in self.hand:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        for rank, count in list(rank_counts.items()):
            if count == 4:
                self.books.append(rank)
                self.hand = [c for c in self.hand if c.rank != rank]
                print(f"{self.name} completed a book of {rank}s!")

    def __str__(self):
        return f"{self.name} has {len(self.hand)} cards and {len(self.books)} books."


class SmartAI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.memory = set()  # remembers ranks seen or heard

    def remember_rank(self, rank):
        """Store a rank in memory for future asking."""
        if rank in RANKS:
            self.memory.add(rank)

    def choose_rank(self):
        """Choose a rank to ask for based on memory and current hand."""
        # Prefer ranks in hand
        hand_ranks = {card.rank for card in self.hand}
        possible = list(hand_ranks & self.memory)
        if possible:
            return random.choice(possible)

        # If no memory match, choose from hand
        if hand_ranks:
            return random.choice(list(hand_ranks))

        # If hand is empty, pick random rank
        return random.choice(RANKS)


def go_fish():
    deck = Deck()
    player = Player("Player 1")
    ai = SmartAI("Computer")

    # Deal initial hands
    for _ in range(7):
        player.draw_card(deck)
        ai.draw_card(deck)

    current_player = player
    opponent = ai

    while len(player.books) + len(ai.books) < len(RANKS):
        print("\n" + "-" * 40)
        print(player)
        print(ai)
        print(f"Deck has {len(deck)} cards left.")

        if current_player == player:
            print("Your hand:", ", ".join(f"{c.rank}" for c in player.hand))
            rank = input("Ask for a rank: ").strip().upper()
            if rank not in RANKS:
                print("Invalid rank. Try again.")
                continue

            ai.remember_rank(rank)  # AI remembers what you asked for

        else:
            rank = ai.choose_rank()
            print(f"Computer asks: Do you have any {rank}s?")
            player_rank_list = [c.rank for c in player.hand]
            for r in player_rank_list:
                ai.remember_rank(r)  # AI learns from seeing your cards later

        if rank and opponent.has_rank(rank):
            print(f"{opponent.name} says: Yes! Here you go.")
            cards_given = opponent.give_all_rank(rank)
            current_player.hand.extend(cards_given)

        else:
            print(f"{opponent.name} says: Go Fish!")
            drawn = current_player.draw_card(deck)
            if drawn:
                print(f"{current_player.name} draws {drawn}")
                if isinstance(current_player, SmartAI):
                    current_player.remember_rank(drawn.rank)

            else:
                print("Deck is empty.")

        current_player.check_for_books()

        # Switch turns if no card was gained
        if not (rank and opponent.has_rank(rank)):
            current_player, opponent = opponent, current_player

    # Game over
    print("\nGame Over!")
    print(f"You completed {len(player.books)} books: {player.books}")
    print(f"Computer completed {len(ai.books)} books: {ai.books}")
    if len(player.books) > len(ai.books):
        print("You win!")

    elif len(player.books) < len(ai.books):
        print("Computer wins!")

    else:
        print("It's a tie!")


if __name__ == "__main__":
    go_fish()