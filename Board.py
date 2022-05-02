from dataclasses import dataclass, field
import tkinter as tk
from tkinter import ttk
import random

@dataclass
class Board():
    """Class that holds attributes 
    and methods for the board."""
    super().__init__()
    size: int = field()
    count: int = 0
    game_over: bool = False
    matches: list = [True for x in range(size)]
    matches.extend([False for x in range(size)])
    random.shuffle(matches)
