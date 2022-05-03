from enum import Enum
import tkinter as tk
class TileState(Enum):
    """
    Enum for the state of a tile.
    """
    REVEALED = 0
    HIDDEN = 1

class Button(tk.Button):
    """
    Button class to represent the tiles.
    """
    def __init__(self, master, row, column):
        """
        Initializes the button.
        """
        super().__init__(master, text=' ',
                         state='disabled', width=7, height=4, bg='#f0f0f0')
        self.grid(row=row, column=column)
        self.state = TileState.REVEALED
        self.master = master

    def reveal(self):
        """
        Reveals the tile.
        """
        self.state = TileState.REVEALED
        self.config(bg='black')
    
    def hide(self):
        """
        Hides the tile.
        """
        self.state = TileState.HIDDEN
        self.config(bg='#f0f0f0')

    def disable(self):
        """
        Disables the tile.
        """
        self.config(state='disabled')

    def enable(self):
        """
        Enables the tile.
        """
        self.config(state='normal')