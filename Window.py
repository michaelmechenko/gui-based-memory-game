import tkinter as tk
from tkinter import ttk
from unittest import case
class ParentWindow(tk.Tk):
    """Class that initializes the parent
    window and creates the tabs."""
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Tile Matching Memory Game')
        self.geometry('800x400')
        self.resizable(False, False)
        self.title_label = None
        self.tab_control = None
        self.easy = None
        self.medium = None
        self.hard = None
        self.customize = None

        # create tabs
        self.create_tabs()

    def create_tabs(self):
        """Creates the tabs/frames for the game."""
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
    
    def get_frame(self, frame):
        if frame == 'easy':
            return self.easy
        elif frame == 'medium':
            return self.medium
        elif frame == 'hard':
            return self.hard
        elif frame == 'customize':
            return self.customize

    def start_button(self):
        """Creates the start button."""
        pass

    def reset(self):
        """Resets the game."""
        pass
    
    def add_timer(self):
        """Creates the timer."""
        pass
    
    def create_easy(self):
        """Creates the easy-difficulty frame."""
        pass

    def create_medium(self):
        """Creates the medium-difficulty frame."""
        pass

    def create_hard(self):
        """Creates the hard-difficulty frame."""
        pass

    def create_customize(self):
        """Creates the customizable frame."""
        pass

    def win_screen(self):
        """Displays the win screen."""
        pass

    def lose_screen(self):
        """Displays the lose screen."""
        pass

root = ParentWindow()
root.mainloop()