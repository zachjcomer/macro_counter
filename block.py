import tools

"""
Block: a composite class consisting of an Action class and a Clock class.
"""

def new(**blockConfig):
    return Block(**blockConfig)

class Block:
    def __init__(self, **blockConfig):
        for option, value in blockConfig.items():
            if option.lower().strip() == "name":
                self.name = f'{value}'

    # executes the block's activity and timer
    def run(self):
        print(f'Do block {self.getName()}')
        if not self.clock == None:
            self.clock.start()
        input()

    # returns block name
    def getName(self) -> str:
        return self.name

    # sets block name
    def setName(self):
        name = tools.safeInput(f'Enter new name for {self.getName()}:', [], str)
        self.name = name

    # pretty print the block's components
    def display(self) -> None:
        print(f'{self.getName()}')

    # returns the block's name
    def __str__(self) -> str:
        return self.getName()

    """UNSAFE METHODS BELOW THIS LINE -- USE WITH CAUTION -- DONT PERFORM INPUT VALIDATION OR RANGE CHECKING"""
    def _addClock(self, clock):
        self.clock = clock

    def _deleteClock(self):
        self.clock = None

    def _setName(self, name) -> str:
        self.name = name
        return self