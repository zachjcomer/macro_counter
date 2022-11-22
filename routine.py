import tools
import block

"""
Routine
Container for blocks.
"""

def new(i):
    return Routine(i)

class Routine:
    # routine aggregates block objects
    def __init__(self, i):
        self.name = f'Routine {i}'
        self.blocks = []

    # executes the routine's blocks in order of list appearance
    def run(self):
        print(f'Running {self.getName()}...')
        for block in self.blocks:
            block.run()

    # returns routine name
    def getName(self) -> str:
        return self.name

    # prompts for a new name
    def setName(self, argName):
        if not argName:
            argName = tools.safeInput(f'Enter a new name for {self.getName()}.', [], str)
        self.name = argName
        return self

    # what would need a block outside of a routine? a routine is just a block container -- copying routines maybe?
    def getBlock(self):
        i = self._selectBlock(f'Select a block to modify from {self.getName()}')
        return self.blocks[i]

    # add -> create enforces that an object is being created
    # creates a block object with the given blockConfig and adds it to self.blocks
    def createBlock(self, **blockConfig):
        self.blocks.append(block.new(**blockConfig))
        return self

    # removes the block from self.blocks if valid
    def deleteBlock(self):
        i = self._selectBlock(f'Select a block to delete from {self.getName()}')
        if tools.safeInputSwitch(f'Are you sure you want to delete {self.blocks[i]}?', ['y/n'], ['y', 'n']) == 'y':
            self.blocks.pop(i)

    # swaps blocks at index i,j if possible
    def moveBlock(self):
        i = self._selectBlock(f'Select the first block to swap from {self.getName()}')
        j = self._selectBlock(f'Select the second block to swap from {self.getName()}')
        self.blocks[i], self.blocks[j] = self.blocks[j], self.blocks[i]

    # pretty print the routine's blocks
    def display(self) -> None:
        print(f'{self.getName()} blocks:')
        for i, b in enumerate(self.blocks):
            print(f'{i}. {b}')

    # returns a list of the routine's blocks
    def list(self) -> str:
        out = []
        for block in self.blocks:
            out.append(str(block))
        return out

    # get safe input for selecting a block
    def _selectBlock(self, prompt) -> int:
        return tools.safeInputRange(f'{prompt}', self.list(), int, 0, len(self.blocks))

    # returns the routine's name
    def __str__(self) -> str:
        return self.getName()

    """UNSAFE METHODS BELOW THIS LINE -- USE WITH CAUTION -- DONT PERFORM INPUT VALIDATION OR RANGE CHECKING"""
    def _getBlock(self, i):
        if i < len(self.blocks):
            return self.blocks[i]

    def _createBlock(self, **blockConfig):
        self.blocks.append(block.new(**blockConfig))
        return self

    def _deleteBlock(self, i):
        self.blocks.pop(i)
        return self

    def _moveBlock(self, i, j):
        if i < len(self.blocks) and j < len(self.blocks):
            self.blocks[i], self.blocks[j] = self.blocks[j], self.blocks[i]
        return self
