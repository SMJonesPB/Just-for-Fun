import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# ------------------------------
# Bingo logic helpers
# ------------------------------

def generate_card():
    """Generate a 5x5 Bingo card with BINGO column ranges."""
    card = []
    ranges = [(1, 15), (16, 30), (31, 45), (46, 60), (61, 75)]
    for low, high in ranges:
        nums = random.sample(range(low, high + 1), 5)
        card.append(nums)
    return [list(row) for row in zip(*card)]


def build_patterns():
    """Return dict: pattern_name -> list of list of (r,c) coordinates."""
    patterns = {}

    # Rows
    for r in range(5):
        patterns[f"Row {r+1}"] = [[(r, c) for c in range(5)]]

    # Columns
    for c in range(5):
        patterns[f"Column {c+1}"] = [[(r, c) for r in range(5)]]

    # Diagonals
    patterns["Diagonal TL-BR"] = [[(i, i) for i in range(5)]]
    patterns["Diagonal BL-TR"] = [[(4 - i, i) for i in range(5)]]

    # Four corners
    patterns["Four Corners"] = [[(0, 0), (0, 4), (4, 0), (4, 4)]]

    # Blackout
    patterns["Blackout"] = [[(r, c) for r in range(5) for c in range(5)]]

    # X pattern
    patterns["X"] = [[(i, i) for i in range(5)] + [(4 - i, i) for i in range(5)]]

    # T pattern
    mid = 2
    patterns["T"] = [[(0, c) for c in range(5)] + [(r, mid) for r in range(1, 5)]]

    # Plus sign
    patterns["Plus"] = [[(mid, c) for c in range(5)] + [(r, mid) for r in range(5)]]

    # Diamond
    patterns["Diamond"] = [[
        (0, 2),
        (1, 1), (1, 3),
        (2, 0), (2, 4),
        (3, 1), (3, 3),
        (4, 2)
    ]]

    # Outer ring
    border = []
    for c in range(5):
        border.append((0, c))
        border.append((4, c))
    for r in range(1, 4):
        border.append((r, 0))
        border.append((r, 4))
    patterns["Outer Ring"] = [border]

    return patterns


PATTERNS = build_patterns()


def check_patterns(marked, active_names):
    """Return (pattern_name, coords) if any active pattern is complete."""
    for name, groups in PATTERNS.items():
        if name not in active_names:
            continue
        for group in groups:
            if all(marked[r][c] for r, c in group):
                return name, group
    return None, None


# ------------------------------
# Pattern selector dialog
# ------------------------------

class PatternSelectorDialog:
    def __init__(self, parent, initial_selected=None):
        self.top = tk.Toplevel(parent)
        self.top.title("Select Patterns")
        self.top.configure(bg="#0A5C0A")
        self.top.grab_set()

        tk.Label(self.top, text="Select active patterns for this game:",
                 bg="#0A5C0A", fg="white", font=("Arial", 12, "bold")).pack(pady=5)

        self.vars = {}
        frame = tk.Frame(self.top, bg="#0A5C0A")
        frame.pack(padx=10, pady=5)

        if initial_selected is None:
            initial_selected = list(PATTERNS.keys())

        for i, name in enumerate(sorted(PATTERNS.keys())):
            var = tk.BooleanVar(value=(name in initial_selected))
            cb = tk.Checkbutton(frame, text=name, variable=var,
                                bg="#0A5C0A", fg="white",
                                selectcolor="#0A5C0A",
                                activebackground="#0A5C0A",
                                activeforeground="white", anchor="w")
            cb.grid(row=i // 2, column=i % 2, sticky="w", padx=5, pady=2)
            self.vars[name] = var

        btn_frame = tk.Frame(self.top, bg="#0A5C0A")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="OK", width=10, command=self.on_ok).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="All", width=10, command=self.on_all).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="None", width=10, command=self.on_none).grid(row=0, column=2, padx=5)

        self.result = None

    def on_ok(self):
        selected = [name for name, var in self.vars.items() if var.get()]
        if not selected:
            messagebox.showwarning("Patterns", "Select at least one pattern.")
            return
        self.result = selected
        self.top.destroy()

    def on_all(self):
        for var in self.vars.values():
            var.set(True)

    def on_none(self):
        for var in self.vars.values():
            var.set(False)


# ------------------------------
# BingoCard GUI wrapper
# ------------------------------

class BingoCardGUI:
    def __init__(self, parent, card_id):
        self.parent = parent
        self.card_id = card_id
        self.card = generate_card()
        self.marked = [[False] * 5 for _ in range(5)]
        self.labels = [[None] * 5 for _ in range(5)]
        self.frame = tk.Frame(parent, bd=2, relief="groove", bg="#0A5C0A")

        title = tk.Label(self.frame, text=f"Card {card_id+1}", fg="white",
                         bg="#0A5C0A", font=("Arial", 12, "bold"))
        title.grid(row=0, column=0, columnspan=5, pady=(2, 4))

        for r in range(5):
            for c in range(5):
                val = self.card[r][c]
                lbl = tk.Label(self.frame, text=str(val), width=4, height=2,
                               bg="darkgreen", fg="white", font=("Arial", 12, "bold"),
                               relief="ridge", bd=1)
                lbl.grid(row=r+1, column=c, padx=1, pady=1)
                lbl.bind("<Button-1>", lambda e, rr=r, cc=c: self.toggle_mark(rr, cc))
                self.labels[r][c] = lbl

        self.bingos = 0
        self.matches = 0

    def toggle_mark(self, r, c):
        self.marked[r][c] = not self.marked[r][c]
        self.update_cell_color(r, c)

    def update_cell_color(self, r, c, highlight=False):
        if highlight:
            self.labels[r][c].config(bg="yellow", fg="black")
        else:
            if self.marked[r][c]:
                self.labels[r][c].config(bg="gold", fg="black")
            else:
                self.labels[r][c].config(bg="darkgreen", fg="white")

    def mark_number(self, num):
        hit = False
        for r in range(5):
            for c in range(5):
                if self.card[r][c] == num and not self.marked[r][c]:
                    self.marked[r][c] = True
                    self.matches += 1
                    self.update_cell_color(r, c)
                    hit = True
        return hit

    def check_bingo(self, active_patterns):
        return check_patterns(self.marked, active_patterns)

    def highlight_pattern(self, coords):
        for r, c in coords:
            self.update_cell_color(r, c, highlight=True)


# ------------------------------
# Main Game GUI
# ------------------------------

class BingoGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Card Bingo")
        self.root.configure(bg="#0A5C0A")

        self.cards = []
        self.called_numbers = set()
        self.call_order = []
        self.current_call = None

        self.active_patterns = list(PATTERNS.keys())
        self.pattern_wins = {name: 0 for name in PATTERNS}

        # Stats
        self.games_played = 0
        self.games_won = 0
        self.fastest_bingo = None
        self.slowest_bingo = None
        self.total_calls_for_wins = 0

        # Top controls
        top_frame = tk.Frame(root, bg="#0A5C0A")
        top_frame.pack(side="top", fill="x", pady=5)

        self.call_label = tk.Label(top_frame, text="Last Call: --",
                                   font=("Arial", 16, "bold"),
                                   bg="#0A5C0A", fg="white")
        self.call_label.grid(row=0, column=0, padx=10)

        self.pattern_label = tk.Label(top_frame, text="Pattern: --",
                                      font=("Arial", 12),
                                      bg="#0A5C0A", fg="white")
        self.pattern_label.grid(row=0, column=1, padx=10)

        self.auto_var = tk.BooleanVar(value=True)
        self.auto_check = tk.Checkbutton(
            top_frame, text="Auto-daub", variable=self.auto_var,
            bg="#0A5C0A", fg="white", selectcolor="#0A5C0A",
            activebackground="#0A5C0A", activeforeground="white"
        )
        self.auto_check.grid(row=0, column=2, padx=10)

        self.call_button = tk.Button(top_frame, text="Call Number",
                                     command=self.call_number, width=12)
        self.call_button.grid(row=0, column=3, padx=10)

        self.new_game_button = tk.Button(top_frame, text="New Game",
                                         command=self.new_game, width=12)
        self.new_game_button.grid(row=0, column=4, padx=10)

        self.reset_button = tk.Button(top_frame, text="Reset Stats",
                                      command=self.reset_stats, width=12)
        self.reset_button.grid(row=0, column=5, padx=10)

        # Middle frame: cards (left) + stats (right)
        middle_frame = tk.Frame(root, bg="#0A5C0A")
        middle_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        self.cards_frame = tk.Frame(middle_frame, bg="#0A5C0A")
        self.cards_frame.pack(side="left", padx=10, pady=10)

        self.stats_frame = tk.Frame(middle_frame, bg="#0A5C0A", bd=2, relief="groove")
        self.stats_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        tk.Label(self.stats_frame, text="Stats", bg="#0A5C0A", fg="white",
                 font=("Arial", 12, "bold")).pack(anchor="w", pady=(2, 4), padx=4)

        self.stats_label = tk.Label(self.stats_frame, text="", bg="#0A5C0A",
                                    fg="white", font=("Arial", 10), justify="left")
        self.stats_label.pack(fill="both", expand=True, padx=4, pady=4, anchor="nw")

        self.new_game(first=True)

    def new_game(self, first=False):
        if not first:
            if not messagebox.askyesno("New Game", "Start a new game?"):
                return

        for widget in self.cards_frame.winfo_children():
            widget.destroy()
        self.cards.clear()

        self.called_numbers.clear()
        self.call_order.clear()
        self.current_call = None
        self.call_label.config(text="Last Call: --")
        self.pattern_label.config(text="Pattern: --")

        num_cards = simpledialog.askinteger(
            "Cards", "How many cards? (1-4)", minvalue=1, maxvalue=4
        )
        if not num_cards:
            num_cards = 1

        dlg = PatternSelectorDialog(self.root, initial_selected=self.active_patterns)
        self.root.wait_window(dlg.top)
        if dlg.result:
            self.active_patterns = dlg.result
        else:
            self.active_patterns = list(PATTERNS.keys())

        for i in range(num_cards):
            card_gui = BingoCardGUI(self.cards_frame, i)
            row = i // 2
            col = i % 2
            card_gui.frame.grid(row=row, column=col, padx=10, pady=10)
            self.cards.append(card_gui)

        self.games_played += 1
        self.update_stats()

    def call_number(self):
        if len(self.called_numbers) >= 75:
            messagebox.showinfo("End", "All numbers have been called.")
            return

        while True:
            num = random.randint(1, 75)
            if num not in self.called_numbers:
                break

        self.called_numbers.add(num)
        self.call_order.append(num)
        self.current_call = num

        letter = self.get_letter(num)
        self.call_label.config(text=f"Last Call: {letter} {num}")

        if self.auto_var.get():
            for card in self.cards:
                card.mark_number(num)

        any_bingo = False
        winning_patterns = []

        for card in self.cards:
            pattern_name, coords = card.check_bingo(self.active_patterns)
            if pattern_name:
                any_bingo = True
                card.bingos += 1
                card.highlight_pattern(coords)
                winning_patterns.append(pattern_name)
                self.pattern_wins[pattern_name] += 1

        if any_bingo:
            self.games_won += 1
            calls = len(self.call_order)
            if self.fastest_bingo is None or calls < self.fastest_bingo:
                self.fastest_bingo = calls
            if self.slowest_bingo is None or calls > self.slowest_bingo:
                self.slowest_bingo = calls
            self.total_calls_for_wins += calls

            unique_patterns = ", ".join(sorted(set(winning_patterns)))
            self.pattern_label.config(text=f"Pattern: {unique_patterns}")
            messagebox.showinfo("BINGO!", f"Bingo achieved!\nPatterns: {unique_patterns}")
            self.update_stats()

    def reset_stats(self):
        if not messagebox.askyesno("Reset Stats", "Reset all stats?"):
            return

        self.games_played = 0
        self.games_won = 0
        self.fastest_bingo = None
        self.slowest_bingo = None
        self.total_calls_for_wins = 0

        for name in self.pattern_wins:
            self.pattern_wins[name] = 0

        for card in self.cards:
            card.bingos = 0
            card.matches = 0

        self.update_stats()

    def get_letter(self, num):
        if 1 <= num <= 15:
            return "B"
        elif 16 <= num <= 30:
            return "I"
        elif 31 <= num <= 45:
            return "N"
        elif 46 <= num <= 60:
            return "G"
        else:
            return "O"

    def update_stats(self):
        lines = []
        lines.append(f"Games played: {self.games_played}")
        lines.append(f"Games won: {self.games_won}")
        if self.games_won > 0:
            avg = self.total_calls_for_wins / self.games_won
            lines.append(f"Fastest bingo: {self.fastest_bingo} calls")
            lines.append(f"Slowest bingo: {self.slowest_bingo} calls")
            lines.append(f"Average calls to bingo: {avg:.1f}")
        else:
            lines.append("Fastest bingo: --")
            lines.append("Slowest bingo: --")
            lines.append("Average calls to bingo: --")

        for i, card in enumerate(self.cards):
            lines.append(f"Card {i+1}: bingos={card.bingos}, matches={card.matches}")

        lines.append("")
        lines.append("Pattern Stats:")
        for name in sorted(self.active_patterns):
            wins = self.pattern_wins[name]
            lines.append(f"  {name}: {wins} win{'s' if wins != 1 else ''}")

        self.stats_label.config(text="\n".join(lines))


if __name__ == "__main__":
    root = tk.Tk()
    app = BingoGameGUI(root)
    root.mainloop()