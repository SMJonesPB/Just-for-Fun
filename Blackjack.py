import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import random
import os

# ------------------------------
# Blackjack Engine
# ------------------------------

CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = list(CARD_VALUES.keys())
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = sum(CARD_VALUES[card[:-1]] for card in hand)
    aces = sum(1 for card in hand if card.startswith('A'))
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

def hand_type(hand):
    """Return 'Soft' if the hand contains an Ace counted as 11, else 'Hard'."""
    value = calculate_hand_value(hand)
    # Count aces
    aces = sum(1 for card in hand if card.startswith('A'))

    # If any ace can be counted as 11 without busting, it's soft
    if aces > 0:
        # Try counting one ace as 11
        if value + 10 <= 21:
            return "Soft"
        
    return "Hard"



# ------------------------------
# GUI Class
# ------------------------------

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Casino")
        self.root.configure(bg="#0A5C0A")

        # Game state
        self.chips = 500
        self.bet = 0
        self.insurance_bet = 0
        self.deck = []
        self.player_hands = []   # list of dicts: {"cards": [...], "bet": x, "result": str}
        self.active_hand_index = 0
        self.dealer_hand = []

        # Load card images (using your naming convention)
        self.load_card_images()

        # Dealer area
        self.dealer_frame = tk.Frame(root, bg="#0A5C0A")
        self.dealer_frame.pack(pady=10)
        tk.Label(self.dealer_frame, text="Dealer", font=("Arial", 20),
                 bg="#0A5C0A", fg="white").pack()
        self.dealer_cards_frame = tk.Frame(self.dealer_frame, bg="#0A5C0A")
        self.dealer_cards_frame.pack()

        # Player area
        self.player_frame = tk.Frame(root, bg="#0A5C0A")
        self.player_frame.pack(pady=10)
        tk.Label(self.player_frame, text="Player", font=("Arial", 20),
                 bg="#0A5C0A", fg="white").pack()
        self.player_cards_frame = tk.Frame(self.player_frame, bg="#0A5C0A")
        self.player_cards_frame.pack()

        # Info
        self.info_label = tk.Label(root, text="Chips: 500", font=("Arial", 16),
                                   bg="#0A5C0A", fg="white")
        self.info_label.pack(pady=10)

        # Buttons
        self.button_frame = tk.Frame(root, bg="#0A5C0A")
        self.button_frame.pack(pady=10)

        self.hit_btn = tk.Button(self.button_frame, text="Hit", width=10, command=self.hit)
        self.stand_btn = tk.Button(self.button_frame, text="Stand", width=10, command=self.stand)
        self.double_btn = tk.Button(self.button_frame, text="Double", width=10, command=self.double)
        self.surrender_btn = tk.Button(self.button_frame, text="Surrender", width=10, command=self.surrender)
        self.split_btn = tk.Button(self.button_frame, text="Split", width=10, command=self.split)
        self.deal_btn = tk.Button(self.button_frame, text="Deal", width=10, command=self.start_round)

        self.hit_btn.grid(row=0, column=0, padx=5)
        self.stand_btn.grid(row=0, column=1, padx=5)
        self.double_btn.grid(row=0, column=2, padx=5)
        self.surrender_btn.grid(row=0, column=3, padx=5)
        self.split_btn.grid(row=0, column=4, padx=5)
        self.deal_btn.grid(row=0, column=5, padx=5)

        self.disable_action_buttons()

    # ------------------------------
    # Load Card Images (your naming convention)
    # ------------------------------

    def load_card_images(self):
        self.card_images = {}
        path = "Card Pictures"

        suit_names = {
            "♠": "spades",
            "♥": "hearts",
            "♦": "diamonds",
            "♣": "clubs"
        }

        rank_names = {
            "A": "ace",
            "J": "jack",
            "Q": "queen",
            "K": "king"
        }

        for filename in os.listdir(path):
            if filename.endswith(".png") and filename != "back.png":
                name = filename.replace(".png", "")  # e.g. "ace of clubs"
                parts = name.split(" of ")
                if len(parts) != 2:
                    continue
                rank_word, suit_word = parts

                # rank word -> rank symbol
                rank = None
                for r, w in rank_names.items():
                    if w == rank_word:
                        rank = r
                        break
                if rank is None:
                    rank = rank_word  # numeric ranks like "5"

                # suit word -> suit symbol
                suit = None
                for s, w in suit_names.items():
                    if w == suit_word:
                        suit = s
                        break
                if suit is None:
                    continue

                card_key = f"{rank}{suit}"

                img = Image.open(os.path.join(path, filename))
                img = img.resize((80, 120), Image.LANCZOS)
                self.card_images[card_key] = ImageTk.PhotoImage(img)

        back = Image.open(os.path.join(path, "back.png"))
        back = back.resize((80, 120), Image.LANCZOS)
        self.card_back = ImageTk.PhotoImage(back)

    # ------------------------------
    # Display
    # ------------------------------

    def update_display(self, hide_dealer=False):
        for w in self.dealer_cards_frame.winfo_children():
            w.destroy()
        for w in self.player_cards_frame.winfo_children():
            w.destroy()

        # Dealer cards
        for i, card in enumerate(self.dealer_hand):
            if hide_dealer and i == 0:
                lbl = tk.Label(self.dealer_cards_frame, image=self.card_back, bg="#0A5C0A")
            else:
                lbl = tk.Label(self.dealer_cards_frame, image=self.card_images[card], bg="#0A5C0A")
            lbl.pack(side="left", padx=5)

        # Player active hand
        if self.player_hands:
            active_hand = self.player_hands[self.active_hand_index]["cards"]
            for card in active_hand:
                lbl = tk.Label(self.player_cards_frame, image=self.card_images[card], bg="#0A5C0A")
                lbl.pack(side="left", padx=5)

        # Show soft/hard for the active player hand
        if self.player_hands:
            active = self.player_hands[self.active_hand_index]["cards"]
            p_value = calculate_hand_value(active)
            p_type = hand_type(active)
            player_text = f"Player: {p_value} ({p_type})"
            
        else:
            player_text = ""

        # Show soft/hard for dealer if revealed
        if not hide_dealer:
            d_value = calculate_hand_value(self.dealer_hand)
            d_type = hand_type(self.dealer_hand)
            dealer_text = f"Dealer: {d_value} ({d_type})"


        else:
            dealer_text = "Dealer: ??"

        self.info_label.config(
            text=f"Chips: {self.chips}    Bet: {self.bet}    {player_text}    {dealer_text}"
        )

    # ------------------------------
    # Button State Helpers
    # ------------------------------

    def disable_action_buttons(self):
        for btn in (self.hit_btn, self.stand_btn, self.double_btn, self.surrender_btn, self.split_btn):
            btn.config(state="disabled")

    def enable_action_buttons(self):
        for btn in (self.hit_btn, self.stand_btn, self.double_btn, self.surrender_btn):
            btn.config(state="normal")

    # ------------------------------
    # Round Start
    # ------------------------------

    def start_round(self):
        if self.chips <= 0:
            messagebox.showinfo("Game Over", "You're out of chips!")
            return

        bet = simpledialog.askinteger("Bet", f"You have {self.chips} chips. Enter bet:",
                                      minvalue=1, maxvalue=self.chips)
        if not bet:
            return

        self.bet = bet
        self.chips -= bet
        self.insurance_bet = 0

        self.deck = create_deck()
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.player_hands = [{"cards": [self.deck.pop(), self.deck.pop()],
                              "bet": bet, "result": ""}]
        self.active_hand_index = 0

        self.update_display(hide_dealer=True)
        self.enable_action_buttons()
        self.split_btn.config(state="disabled")

        # Split availability
        ph = self.player_hands[0]["cards"]
        if ph[0][:-1] == ph[1][:-1] and self.chips >= bet:
            self.split_btn.config(state="normal")

        # Insurance
        if self.dealer_hand[1].startswith("A"):
            self.offer_insurance()

        # Dealer blackjack
        if calculate_hand_value(self.dealer_hand) == 21:
            self.reveal_dealer_blackjack()

    # ------------------------------
    # Insurance
    # ------------------------------

    def offer_insurance(self):
        if messagebox.askyesno("Insurance", "Dealer shows an Ace. Take insurance?"):
            insurance = self.bet // 2
            if self.chips >= insurance:
                self.insurance_bet = insurance
                self.chips -= insurance
                self.update_display(hide_dealer=True)
            else:
                messagebox.showinfo("Insurance", "Not enough chips for insurance.")

    def reveal_dealer_blackjack(self):
        self.update_display(hide_dealer=False)
        messagebox.showinfo("Blackjack", "Dealer has blackjack!")

        # Insurance payout: break-even overall if taken
        if self.insurance_bet > 0:
            self.chips += self.insurance_bet * 3  # stake + 2:1 payout

        ph = self.player_hands[0]["cards"]
        if calculate_hand_value(ph) == 21:
            # Push on blackjack vs blackjack
            self.chips += self.bet

        self.disable_action_buttons()

    # ------------------------------
    # Player Actions
    # ------------------------------

    def hit(self):
        hand = self.player_hands[self.active_hand_index]["cards"]
        hand.append(self.deck.pop())
        self.update_display(hide_dealer=True)

        if calculate_hand_value(hand) > 21:
            messagebox.showinfo("Bust", "You busted!")
            self.player_hands[self.active_hand_index]["result"] = "bust"
            self.finish_or_next_hand()

    def stand(self):
        self.player_hands[self.active_hand_index]["result"] = "stand"
        self.finish_or_next_hand()

    def double(self):
        hand_info = self.player_hands[self.active_hand_index]
        if self.chips < hand_info["bet"]:
            messagebox.showinfo("Error", "Not enough chips to double.")
            return

        self.chips -= hand_info["bet"]
        hand_info["bet"] *= 2
        hand_info["cards"].append(self.deck.pop())
        self.update_display(hide_dealer=True)

        if calculate_hand_value(hand_info["cards"]) > 21:
            hand_info["result"] = "bust"
        else:
            hand_info["result"] = "stand"

        self.finish_or_next_hand()

    def surrender(self):
        self.player_hands[self.active_hand_index]["result"] = "surrender"
        self.finish_or_next_hand()

    def split(self):
        hand = self.player_hands[0]["cards"]
        if self.chips < self.bet:
            messagebox.showinfo("Error", "Not enough chips to split.")
            return

        self.chips -= self.bet

        h1 = [hand[0], self.deck.pop()]
        h2 = [hand[1], self.deck.pop()]

        self.player_hands = [
            {"cards": h1, "bet": self.bet, "result": ""},
            {"cards": h2, "bet": self.bet, "result": ""}
        ]

        self.active_hand_index = 0
        self.split_btn.config(state="disabled")
        self.update_display(hide_dealer=True)

    # ------------------------------
    # Hand Flow
    # ------------------------------

    def finish_or_next_hand(self):
        if self.active_hand_index + 1 < len(self.player_hands):
            self.active_hand_index += 1
            self.update_display(hide_dealer=True)

        else:
            self.disable_action_buttons()
            self.dealer_play()

    # ------------------------------
    # Dealer + Results
    # ------------------------------

    def dealer_play(self):
        while calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())

        self.update_display(hide_dealer=False)
        dealer_value = calculate_hand_value(self.dealer_hand)

        for hand_info in self.player_hands:
            result = hand_info["result"]
            bet = hand_info["bet"]
            value = calculate_hand_value(hand_info["cards"])

            if result == "surrender":
                self.chips += bet // 2
                continue

            if result == "bust":
                continue

            if dealer_value > 21 or value > dealer_value:
                self.chips += bet * 2

            elif value == dealer_value:
                self.chips += bet

        self.update_display(hide_dealer=False)


# ------------------------------
# Run GUI
# ------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()
