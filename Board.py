from dataclasses import dataclass, field
import tkinter as tk
import random
from Tile import Button
from Tile import TileState

@dataclass
class Board():
    """Class that holds attributes 
    and methods for the board."""
    size: int
    frame: tk.Frame = field()
    board = {}
    count: int = 0
    game_over: bool = False
    matches = []

    def initialize_matches(self):
        """Initialize list that holds button matches."""
        hf = (self.size * self.size) // 2
        self.matches.append([True for _ in range(hf)])
        self.matches.append([False for _ in range(hf)])
        random.shuffle(self.matches)

    def initialize_board(self):
        """Initializes the buttons on the board."""
        for i in range(self.size):
            for j in range(self.size):
                button_str = 'b' + str(i) + str(j)
                self.board[button_str] = Button(self.frame, 
                    command=lambda: self.on_click(self.board[button_str]), row=i, column=j)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.pack(pady=10)

    def on_click(self, button):
        """Handles button click events."""
        if button.state == TileState.HIDDEN:
            button.disable().reveal()
            self.count += 1
        else:
            self.game_over = True
    
    def show_board(self):
        """Displays the board."""
        for btn in self.board.keys():
            btn.disable().reveal()

    def check_win(self):
        """Checks game state."""
        return self.count == (self.size * self.size) // 2 and self.game_over == True