from enum import Enum
import tkinter as tk
from tkinter import ttk
import random

class TileState(Enum):
    """
    Enum for the state of a tile.
    """
    HIDDEN = 0
    REVEALED = 1

class Button(tk.Button):
    """
    Button class to represent the tiles.
    """
    def __init__(self, master, tile, row, column):
        """
        Initializes the button.
        """
        super().__init__(master, text='', font=('Arial', 20),
                         command=lambda: self.reveal(tile, row, column))
        self.grid(row=row, column=column)
        self.state = TileState.HIDDEN
        self.row = row
        self.column = column
        self.tile = tile
        self.master = master

    def reveal(self, tile, row, column):
        """
        Reveals the tile.
        """
        if self.state == TileState.HIDDEN:
            self.state = TileState.REVEALED
            self.config(text=tile.value)
            self.master.check_match(row, column)