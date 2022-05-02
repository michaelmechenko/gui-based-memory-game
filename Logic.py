from Board import Board
from dataclasses import dataclass, field
@dataclass
class Logic():
    """Class containing methods that 
    manage game state."""
    board: Board = field()

    def on_click(self):
        """Handles button click events."""
        pass

    def get_game_state(self):
        """Checks game state."""
        pass