# tic_tac_toe/logic/models.py

# importing the "enum" function which are pythons versions of gloabl
# variables allow us to use enumerations in python
# "CROSS" & "NAUGHT" have been assigned as the global variables for 
# "X" & "Y" respectably 


import enum

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
