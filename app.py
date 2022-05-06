# didnt fix any of this whoops
import tkinter as tk
from tkinter import ttk
import random
class TileMatching(tk.Tk):
    """Class that controls window creation."""
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Tile Matching Memory Game')
        self.geometry('800x400')
        self.resizable(False, False)
        self.main_window = None
        self.title_label = None

        # create the main window
        self.create_window()

        # logic
        self.count = 0
        self.game_over = False
        self.matches = [True for x in range(8)]
        self.matches.extend([False for x in range(8)])
        random.shuffle(self.matches)

        # creates grid, waits 3 seconds, and then clears the grid
        self.show_grid()
        self.after(3000, self.clear_grid)

    def create_window(self):
        # create the main window
        self.main_window = tk.Frame(self, bg='#f0f0f0')

        # create title label
        self.title_label = ttk.Label(
            self, text='Tile Matching Memory Game', font=('Arial', 20))
        self.title_label.pack(pady=10)

    def clear_grid(self):
        global b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15
        # buttons
        b0 = tk.Button(self.main_window, text=' ', width=7, height=4,
                       command=lambda: self.button_click(b0), bg='#f0f0f0')
        b1 = tk.Button(self.main_window, text=' ', width=7, height=4,
                       command=lambda: self.button_click(b1), bg='#f0f0f0')
        b2 = tk.Button(self.main_window, text=' ', width=7, height=4,
                       command=lambda: self.button_click(b2), bg='#f0f0f0')
        b3 = tk.Button(self.main_window, text=' ', width=7, height=4,
                       command=lambda: self.button_click(b3), bg='#f0f0f0')
        b4 = tk.Button(self.main_window, text=' ', width=7, height=4,
                       command=lambda: self.button_click(b4), bg='#f0f0f0')
        b5 = tk.Button(self.main_window, text=' ', width=7, height=4,
                       command=lambda: self.button_click(b5), bg='#f0f0f0')
        b6 = tk.Button(self.main_window, text=' ', width=7, height=4,
                       command=lambda: self.button_click(b6), bg='#f0f0f0')
        b7 = tk.Button(self.main_window, text=' ', width=7, height=4,
                       command=lambda: self.button_click(b7), bg='#f0f0f0')
        b8 = tk.Button(self.main_window, text=' ', width=7, height=4,
                       command=lambda: self.button_click(b8), bg='#f0f0f0')
        b9 = tk.Button(self.main_window, text=' ', width=7, height=4,
                       command=lambda: self.button_click(b9), bg='#f0f0f0')
        b10 = tk.Button(self.main_window, text=' ', width=7, height=4,
                        command=lambda: self.button_click(b10), bg='#f0f0f0')
        b11 = tk.Button(self.main_window, text=' ', width=7, height=4,
                        command=lambda: self.button_click(b11), bg='#f0f0f0')
        b12 = tk.Button(self.main_window, text=' ', width=7, height=4,
                        command=lambda: self.button_click(b12), bg='#f0f0f0')
        b13 = tk.Button(self.main_window, text=' ', width=7, height=4,
                        command=lambda: self.button_click(b13), bg='#f0f0f0')
        b14 = tk.Button(self.main_window, text=' ', width=7, height=4,
                        command=lambda: self.button_click(b14), bg='#f0f0f0')
        b15 = tk.Button(self.main_window, text=' ', width=7, height=4,
                        command=lambda: self.button_click(b15), bg='#f0f0f0')
        b0.grid(row=0, column=0)
        b1.grid(row=0, column=1)
        b2.grid(row=0, column=2)
        b3.grid(row=0, column=3)
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)
        b7.grid(row=1, column=3)
        b8.grid(row=2, column=0)
        b9.grid(row=2, column=1)
        b10.grid(row=2, column=2)
        b11.grid(row=2, column=3)
        b12.grid(row=3, column=0)
        b13.grid(row=3, column=1)
        b14.grid(row=3, column=2)
        b15.grid(row=3, column=3)
        self.main_window.grid_columnconfigure(0, weight=1)
        self.main_window.pack(pady=10)

    def show_grid(self):
        # buttons
        b0 = tk.Button(self.main_window, text=' ',
                       width=7, height=4, state='disabled')
        b1 = tk.Button(self.main_window, text=' ',
                       width=7, height=4, state='disabled')
        b2 = tk.Button(self.main_window, text=' ',
                       width=7, height=4, state='disabled')
        b3 = tk.Button(self.main_window, text=' ',
                       width=7, height=4, state='disabled')
        b4 = tk.Button(self.main_window, text=' ',
                       width=7, height=4, state='disabled')
        b5 = tk.Button(self.main_window, text=' ',
                       width=7, height=4, state='disabled')
        b6 = tk.Button(self.main_window, text=' ',
                       width=7, height=4, state='disabled')
        b7 = tk.Button(self.main_window, text=' ',
                       width=7, height=4, state='disabled')
        b8 = tk.Button(self.main_window, text=' ',
                       width=7, height=4, state='disabled')
        b9 = tk.Button(self.main_window, text=' ',
                       width=7, height=4, state='disabled')
        b10 = tk.Button(self.main_window, text=' ',
                        width=7, height=4, state='disabled')
        b11 = tk.Button(self.main_window, text=' ',
                        width=7, height=4, state='disabled')
        b12 = tk.Button(self.main_window, text=' ',
                        width=7, height=4, state='disabled')
        b13 = tk.Button(self.main_window, text=' ',
                        width=7, height=4, state='disabled')
        b14 = tk.Button(self.main_window, text=' ',
                        width=7, height=4, state='disabled')
        b15 = tk.Button(self.main_window, text=' ',
                        width=7, height=4, state='disabled')
        b0.grid(row=0, column=0)
        b1.grid(row=0, column=1)
        b2.grid(row=0, column=2)
        b3.grid(row=0, column=3)
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)
        b7.grid(row=1, column=3)
        b8.grid(row=2, column=0)
        b9.grid(row=2, column=1)
        b10.grid(row=2, column=2)
        b11.grid(row=2, column=3)
        b12.grid(row=3, column=0)
        b13.grid(row=3, column=1)
        b14.grid(row=3, column=2)
        b15.grid(row=3, column=3)
        self.main_window.grid_columnconfigure(0, weight=1)

        buttons = [b0, b1, b2, b3, b4, b5, b6, b7,
                   b8, b9, b10, b11, b12, b13, b14, b15]
        button_entries = dict(zip(buttons, self.matches))
        for button in button_entries.keys():
            if button_entries[button] == True:
                button.config(bg='black')
        self.main_window.pack(pady=10)

    def button_click(self, button):
        buttons = [b0, b1, b2, b3, b4, b5, b6, b7,
                   b8, b9, b10, b11, b12, b13, b14, b15]
        button_entries = dict(zip(buttons, self.matches))

        if button_entries[button] == True:
            button.config(bg='black', state='disabled')
            self.count += 1
        else:
            self.game_over = True

        self.check_game_state()

    def check_game_state(self):
        if self.game_over == False and self.count == 8:
            self.main_window.destroy()
            self.title_label.destroy()
            # create the main window
            self.main_window = tk.Frame(self, bg='#f0f0f0')

            # create title label
            self.win_label = ttk.Label(
                self, text='You Won!', font=('Arial', 20))
            self.win_label.pack(pady=175)
        elif self.game_over == True:
            self.main_window.destroy()
            self.title_label.destroy()
            # create the main window
            self.main_window = tk.Frame(self, bg='#f0f0f0')

            # create title label
            self.loss_label = ttk.Label(
                self, text='You Lost!', font=('Arial', 20))
            self.loss_label.pack(pady=175)

def main():
    root = TileMatching()
    root.mainloop()

if __name__ == "__main__":
    main()