import tools

"""
COMPOSITE Block
* consisting of an Action class and a Clock class.

Implementations I can think of rn: lifting -- (set/rep/weight, cooldown timer), calesthenics -- (set/rep, cooldown), HIIT training -- (interval timer), cardio -- (stopwatch/timer)
"""

def new(**blockConfig):
    return Block(**blockConfig)

class Block:
    def __init__(self, **blockConfig):
        for option, value in blockConfig.items():
            if option.lower().strip() == "name":
                self.name = f'{value}'
        self.clock = None

    # executes the block's activity and timer
    def run(self):
        print(f'Do block {self.get_name()}')
        if not self.clock == None:
            self.clock.start()
        input()

    # returns block name
    def get_name(self) -> str:
        return self.name

    # sets block name
    def set_name(self):
        name = tools.safeInput(f'Enter new name for {self.get_name()}:', [], str)
        self.name = name

    # pretty print the block's components
    def display(self) -> None:
        print(f'{self.get_name()}')

    # returns the block's name
    def __str__(self) -> str:
        return self.get_name()

    """UNSAFE METHODS BELOW THIS LINE -- USE WITH CAUTION -- DONT PERFORM INPUT VALIDATION OR RANGE CHECKING"""
    def _add_clock(self, clock):
        self.clock = clock

    def _delete_clock(self):
        self.clock = None

    def _set_name(self, name) -> str:
        self.name = name
        return self