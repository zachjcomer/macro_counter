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
        self.blocks = list()

    # executes the routine's blocks in order of list appearance
    def run(self):
        print(f'Running {self.get_name()}...')
        for block in self.blocks:
            block.run()

    # returns routine name
    def get_name(self) -> str:
        return self.name

    # prompts for a new name
    def set_name(self, argName):
        if not argName:
            argName = tools.safeInput(f'Enter a new name for {self.get_name()}.', [], str)
        self.name = argName
        return self

    # what would need a block outside of a routine? a routine is just a block container -- copying routines maybe?
    def get_block(self):
        i = self._select_block(f'Select a block to modify from {self.get_name()}')
        return self.blocks[i]

    # add -> create enforces that an object is being created
    # creates a block object with the given blockConfig and adds it to self.blocks
    def createBlock(self, **blockConfig):
        self.blocks.append(block.new(**blockConfig))
        return self

    # removes the block from self.blocks if valid
    def deleteBlock(self):
        i = self._select_block(f'Select a block to delete from {self.get_name()}')
        if tools.safeInputSwitch(f'Are you sure you want to delete {self.blocks[i]}?', ['y/n'], ['y', 'n']) == 'y':
            self.blocks.pop(i)

    # swaps blocks at index i,j if possible
    def moveBlock(self):
        i = self._select_block(f'Select the first block to swap from {self.get_name()}')
        j = self._select_block(f'Select the second block to swap from {self.get_name()}')
        self.blocks[i], self.blocks[j] = self.blocks[j], self.blocks[i]

    # pretty print the routine's blocks
    def display(self) -> None:
        print(f'{self.get_name()} blocks:')
        for i, b in enumerate(self.blocks):
            print(f'{i}. {b}')

    # returns a list of the routine's blocks
    def list(self) -> str:
        out = list()
        for block in self.blocks:
            out.append(str(block))
        return out

    # get safe input for selecting a block
    def _select_block(self, prompt) -> int:
        return tools.safeInputRange(f'{prompt}', self.list(), int, 0, len(self.blocks))

    # returns the routine's name
    def __str__(self) -> str:
        return self.get_name()

    """UNSAFE METHODS BELOW THIS LINE -- USE WITH CAUTION -- DONT PERFORM INPUT VALIDATION OR RANGE CHECKING"""
    def _get_block(self, i):
        if i < len(self.blocks):
            return self.blocks[i]

    def _create_block(self, **blockConfig):
        self.blocks.append(block.new(**blockConfig))
        return self

    def _delete_block(self, i):
        self.blocks.pop(i)
        return self

    def _move_block(self, i, j):
        if i < len(self.blocks) and j < len(self.blocks):
            self.blocks[i], self.blocks[j] = self.blocks[j], self.blocks[i]
        return self
