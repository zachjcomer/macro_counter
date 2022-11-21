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
        self.blocks = [ ]

    # returns routine name
    def getName(self) -> str:
        return self.name

    # prompts for a new name
    def setName(self, argName):
        if not argName:
            argName = tools.safeInput(f'Enter a new name for {self.name}.', [], str)
        self.name = argName

        return self

    # what would need a block outside of a routine? a routine is just a block container -- copying routines maybe?
    def getBlock(self, i):
        if i < len(self.blocks):
            return self.blocks[i]

    # add -> create enforces that an object is being created
    # creates a block object with the given blockConfig and adds it to self.blocks
    def createBlock(self, **blockConfig):
        self.blocks.append(block.new(**blockConfig))
        return self

    # removes the block from self.blocks if valid
    def deleteBlock(self) -> bool:
        i = tools.safeInputRange(f'Select a block to delete from {self.name}', self.list(), int, 0, len(self.blocks))
        if tools.safeInputSwitch(f'Are you sure you want to delete {self.blocks[i]}?', ['y/n'], ['y', 'n']) == 'y':
            self.blocks.pop(i)

    def moveBlock(self, i, j) -> bool:
        # swaps blocks at index i,j if possible
        if i < len(self.blocks) and j < len(self.blocks):
            self.blocks[i], self.blocks[j] = self.blocks[j], self.blocks[i]
            return True
        else:
            return False

    def run(self):
        print(f'Running {self.name}...')
        for block in self.blocks:
            block.run()

    def __str__(self) -> str:
        out = f'{self.name}'

        return out

    def _list(self) -> str:
        out = f'{self.name}:\n'
        for block in self.blocks:
            out += f'{block}\n'

        return out

    def list(self) -> str:
        out = []

        for block in self.blocks:
            out.append(str(block))
        return out