import tkinter as tk
from tkinter import ttk

class ParentWindow(tk.Tk):
    """Class that initializes the parent
    window and creates the tabs."""
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Tile Matching Memory Game')
        self.geometry('800x400')
        self.resizable(False, False)
        self.main_window = None
        self.title_label = None

        # create tabs
        self.create_tabs()

    def create_tabs(self):
        """Creates the tabs for the game."""
        tab_control = ttk.Notebook(self)
        easy = ttk.Frame(tab_control)
        medium = ttk.Frame(tab_control)
        hard = ttk.Frame(tab_control)
        customize = ttk.Frame(tab_control)

        tab_control.add(easy, text='Easy')
        tab_control.add(medium, text='Medium')
        tab_control.add(hard, text='Hard')
        tab_control.add(customize, text='Customize')
        tab_control.pack(expand=1, fill='both')

root = ParentWindow()
root.mainloop()