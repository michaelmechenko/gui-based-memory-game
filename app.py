# Michael Mechenko EECE2140

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class TileMatching(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Tile Matching Memory Game')
        self.geometry('800x600')

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()
        

    def button_clicked(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')
    
    def create_grid(self, size):
         for i in range(size):
             for j in range(size):
                 self.Button(self, text='{}x{}'.format(i, j)).grid(row=i, column=j).pack()


if __name__ == "__main__":
    TileMatching = TileMatching()
    TileMatching.mainloop()
    TileMatching.create_grid(10)