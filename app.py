# Michael Mechenko EECE2140

from ctypes import resize
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
import time

class TileMatching(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Tile Matching Memory Game')
        self.geometry('800x600', resize=False)

    def button_clicked(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')
    
    def create_window(self):
         # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

def main():
    root = TileMatching()
    root.create_window()
    tab_control = ttk.Notebook(root)
    easy = ttk.Frame(tab_control)
    medium = ttk.Frame(tab_control)
    hard = ttk.Frame(tab_control)
    tab_control.add(easy, text='Easy')
    tab_control.add(medium, text='Medium')
    tab_control.add(hard, text='Hard')
    tab_control.pack(expand=1, fill='both')
    root.mainloop()


if __name__ == "__main__":
    main()