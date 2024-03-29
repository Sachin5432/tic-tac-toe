# tic_tac_toe/logic/models.py

# importing the "enum" function which are pythons versions of gloabl
# variables allow us to use enumerations in python
# "CROSS" & "NAUGHT" have been assigned as the global variables for 
# "X" & "Y" respectably 

import enum
import re
from dataclasses import dataclass

# we define the class as a string to make it easier to recall the values 
# within the class since they're "X" & "Y"
# "enum.Enum" obviosuly allows the var to be a global var
class Mark(str, enum.Enum):
    # Further sice note, the global var are called with Mark.CROSS/NAUGHT
    #These global var can't be compared to their acc values 
    CROSS = "X"
    NAUGHT = "O"

    # "@property" defines the getter method within the class "Mark"
    # this function assigns a side to the player. ie "X" or "O"
    # or "CROSS" & "NAUGHT"
    @property
    def other(self) -> "Mark":
        # The inner part of this function assigns a side for the other player
        # if self is CROSS it will assignt the other player to NAUGHT 
        # And vice versa
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT

# Line 1 this will update for commit

#class to assigns grid size
@dataclass (frozen=True)
class Grid:
    cells: str = " " * 9
    
#private function to not allow entries that are not "X", "O" or space within the grid
    def __post_init__(self) -> None:
        if not re.match(r"[\sXO]{9}$", self.cells):
            raise ValueError("Must contain 9 cells of: X, O, or space")

    


