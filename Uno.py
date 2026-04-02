import tkinter as tk
from tkinter import messagebox, simpledialog
import random

COLORS = ["Red", "Green", "Blue", "Yellow"]
VALUES = [str(n) for n in range(0, 10)] + ["Skip", "Reverse", "Draw 2"]

def create_deck():
    deck = []
    for color in COLORS:
        deck.append(f"{color} 0")
        for value in VALUES[1:]:
            deck.extend([f"{color} {value}"] * 2)
    for _ in range(4):
        deck.append("Wild")
        deck.append("Wild Draw 4")
    random.shuffle(deck)
    return deck

def can_play(card, top_card, current_color):
    """Check if a card can be played on the current top card."""
    # Wild cards can always be played
    if "Wild" in card:
        return True

    # Split card safely
    card_parts = card.split()
    if len(card_parts) < 2:
        return False

    card_color, card_value = card_parts[0], card_parts[1]

    # If top card is a Wild, match only by chosen color
    if "Wild" in top_card:
        return card_color == current_color

    # Normal case: match by color or value
    top_parts = top_card.split()
    if len(top_parts) >= 2:
        top_color, top_value = top_parts[0], top_parts[1]
        return card_color == current_color or card_value == top_value

    return False

class UnoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("UNO Multiplayer")

        self.num_players = 0
        while self.num_players < 2 or self.num_players > 4:
            try:
                self.num_players = int(simpledialog.askstring("Players", "Enter number of players (2–4):"))
            except (ValueError, TypeError):
                pass

        self.players = []
        for i in range(self.num_players):
            name = simpledialog.askstring("Player Name", f"Enter name for Player {i+1} (type 'CPU' for computer):")
            if not name:
                name = f"Player{i+1}"
            self.players.append(name)

        self.deck = create_deck()
        self.hands = [[self.deck.pop() for _ in range(7)] for _ in range(self.num_players)]
        self.top_card = self.deck.pop()
        while "Wild" in self.top_card:
            self.deck.insert(0, self.top_card)
            random.shuffle(self.deck)
            self.top_card = self.deck.pop()

        self.current_color = self.top_card.split()[0]
        self.direction = 1
        self.turn = 0
        self.skip_next = False
        self.drawn_this_turn = False  # Track if player has drawn

        self.top_label = tk.Label(root, text=f"Top Card: {self.top_card}", font=("Arial", 14))
        self.top_label.pack(pady=10)

        self.color_label = tk.Label(root, text=f"Current Color: {self.current_color}", font=("Arial", 12))
        self.color_label.pack()

        self.info_label = tk.Label(root, text="", font=("Arial", 12))
        self.info_label.pack()

        self.player_frame = tk.Frame(root)
        self.player_frame.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.draw_button = tk.Button(self.button_frame, text="Draw Card", command=self.draw_card)
        self.draw_button.pack(side=tk.LEFT, padx=5)

        self.end_turn_button = tk.Button(self.button_frame, text="End Turn", command=self.end_turn)
        self.end_turn_button.pack(side=tk.LEFT, padx=5)

        self.update_hand_display()

    def update_hand_display(self):
        for widget in self.player_frame.winfo_children():
            widget.destroy()

        current_player = self.players[self.turn]
        self.info_label.config(text=f"{current_player}'s turn")

        if current_player.lower() != "cpu":
            for card in self.hands[self.turn]:
                btn = tk.Button(self.player_frame, text=card, width=12, height=2,
                                command=lambda c=card: self.play_card(c))
                btn.pack(side=tk.LEFT, padx=2)
        else:
            self.root.after(1000, self.cpu_turn)

        self.top_label.config(text=f"Top Card: {self.top_card}")
        self.color_label.config(text=f"Current Color: {self.current_color}")

    def draw_card(self):
        """Human player draws until he/ she has gotten a playable card, then plays it."""
        if self.players[self.turn].lower() == "cpu":
            return  # CPU handled separately

        while True:
            if not self.deck:
                messagebox.showinfo("Deck Empty", "No more cards to draw!")
                break

            drawn_card = self.deck.pop()
            self.hands[self.turn].append(drawn_card)
            self.update_hand_display()

            if can_play(drawn_card, self.top_card, self.current_color):
                # Auto-play the drawn card
                self.hands[self.turn].remove(drawn_card)
                self.top_card = drawn_card
                if "Wild" in drawn_card:
                    self.choose_color()

                else:
                    self.current_color = drawn_card.split()[0]

                self.handle_action_card(drawn_card)
                self.check_winner()
                break  # Stop drawing after playing

        self.next_turn()


    def end_turn(self):
        if self.players[self.turn].lower() != "cpu":
            self.next_turn()

    def play_card(self, card):
        if self.players[self.turn].lower() == "cpu":
            return
        
        if can_play(card, self.top_card, self.current_color):
            self.hands[self.turn].remove(card)
            self.top_card = card
            if "Wild" in card:
                # Ask player for color
                chosen_color = simpledialog.askstring("Choose Color", "Enter color (Red, Green, Blue, Yellow):")
                while chosen_color not in COLORS:
                    chosen_color = simpledialog.askstring("Choose Color", "Enter color (Red, Green, Blue, Yellow):")
                self.current_color = chosen_color
                
            else:
                self.current_color = card.split()[0]


            self.handle_action_card(card)
            self.check_winner()
            self.next_turn()
        else:
            messagebox.showinfo("Invalid Move", "You can't play that card.")

    def choose_color(self):
        color_choice = simpledialog.askstring("Choose Color", "Enter color (Red, Green, Blue, Yellow):")
        if color_choice and color_choice.capitalize() in COLORS:
            self.current_color = color_choice.capitalize()
        else:
            self.current_color = random.choice(COLORS)

    def handle_action_card(self, card):
        if "Skip" in card:
            self.skip_next = True

        elif "Reverse" in card:
            self.direction *= -1

        elif "Draw 2" in card:
            next_player = (self.turn + self.direction) % self.num_players
            self.hands[next_player].extend([self.deck.pop() for _ in range(2)])
            self.skip_next = True

        elif "Wild Draw 4" in card:
            next_player = (self.turn + self.direction) % self.num_players
            self.hands[next_player].extend([self.deck.pop() for _ in range(4)])
            self.skip_next = True

    def cpu_turn(self):
        """CPU draws until it has gotten a playable card, then plays it."""
        playable = [c for c in self.hands[self.turn] if can_play(c, self.top_card, self.current_color)]

        while not playable:
            if not self.deck:
                break  # No cards left to draw

            drawn_card = self.deck.pop()
            self.hands[self.turn].append(drawn_card)
            playable = [c for c in self.hands[self.turn] if can_play(c, self.top_card, self.current_color)]

        if playable:
            card = random.choice(playable)
            self.hands[self.turn].remove(card)
            self.top_card = card
            if "Wild" in card:
                # CPU chooses the color it has the most of
                color_counts = {color: 0 for color in COLORS}
                for c in self.hands[self.turn]:
                    if c.split()[0] in COLORS:
                        color_counts[c.split()[0]] += 1
                self.current_color = max(color_counts, key=color_counts.get)
                print(f"CPU changes color to {self.current_color}")
            else:
                self.current_color = card.split()[0]

                
            self.handle_action_card(card)

        self.check_winner()
        self.next_turn()


    def cpu_choose_color(self):
        """CPU chooses the color it has the most of."""
        color_counts = {color: 0 for color in COLORS}
        for card in self.hands[self.turn]:
            if card.split()[0] in COLORS:
                color_counts[card.split()[0]] += 1

        # Pick the color with the highest count, fallback to random
        best_color = max(color_counts, key=color_counts.get)
        return best_color if color_counts[best_color] > 0 else random.choice(COLORS)
    
    def next_turn(self):
        self.drawn_this_turn = False
        if self.skip_next:
            self.turn = (self.turn + self.direction) % self.num_players
            self.skip_next = False
        self.turn = (self.turn + self.direction) % self.num_players
        self.update_hand_display()

    def check_winner(self):
        if not self.hands[self.turn]:
            messagebox.showinfo("Game Over", f"🎉 {self.players[self.turn]} wins!")
            self.root.destroy()

# === Run Game ===
if __name__ == "__main__":
    root = tk.Tk()
    game = UnoGame(root)
    root.mainloop()