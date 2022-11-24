import tools

"""
COMPOSITE Block
* consisting of an Action class and a Clock class.

Implementations I can think of rn: lifting -- (set/rep/weight, cooldown timer), calesthenics -- (set/rep, cooldown), HIIT training -- (interval timer), cardio -- (stopwatch/timer)
"""

def new():
    return Block()

class Block:
    def __init__(self):
        self.name = 'block'
        self.clock = None
        self.action = None

    # executes the block's activity and timer
    def run(self):
        if not self.clock == None:
            self.clock.start()
        """ if not self.action == None:
            self.action.start() """

    # returns block name
    def get_name(self) -> str:
        return self.name

    # sets block name
    def set_name(self, name):
        self.name = name

    def set_name_safe(self, name) -> str:
        name = tools.safeInput(f'Enter new name for {self.get_name()}:', [], str)
        self.name = name

    # pretty print the block's components
    def display(self) -> None:
        print(f'{self.get_name()}')

    # returns the block's name
    def __str__(self) -> str:
        return self.get_name()

    """UNSAFE METHODS BELOW THIS LINE -- USE WITH CAUTION -- DONT PERFORM INPUT VALIDATION OR RANGE CHECKING"""
