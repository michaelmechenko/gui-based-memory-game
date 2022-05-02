from dataclasses import dataclass, field
import tkinter as tk
import random

from Tile import Button
@dataclass
class Board():
    """Class that holds attributes 
    and methods for the board."""
    super().__init__()
    size: int = field()
    frame: tk.Frame = field()
    board: dict = {}
    count: int = 0
    game_over: bool = False
    matches: list = [True for _ in range(size)]
    matches.extend([False for _ in range(size)])
    random.shuffle(matches)

    def initialize_board(self):
        """Initializes the buttons on the board."""
        for i in range(self.size):
            for j in range(self.size):
                button_str = 'b_r' + str(i) + '_c' + str(j)
                self.board[button_str] = Button(self.frame, row=i, column=j)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.pack(pady=10)