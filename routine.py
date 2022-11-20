import block

def new():
    return Routine()

class Routine:
    def __init__(self):
        self.name = 'Routine'
        self.blocks = [ ]

    def getName(self) -> str:
        # returns str self.name
        return self.name

    def setName(self, newName):
        # attempts to replace self.name with newName.
        # returns self for method chaining.
        if isinstance(newName, str):
            # print(f'Naming {self.name} to {newName}.')
            self.name = newName
        else:
            print(f'Error: Routine#setName requires str but {type(newName).__name__} was supplied.')
        return self

    # what would need a block outside of a routine? a routine is just a block container -- copying routines maybe?
    def getBlock(self, i):
        if i < len(self.blocks):
            return self.blocks[i]

    def addBlock(self, **blockConfig):
        self.blocks.append(block.new(**blockConfig))
        return self

    def delBlock(self, i) -> bool:
        if i < len(self.blocks):
            self.blocks.pop(i)
            return True
        else:
            return False

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
        out = f'{self.name}:\n'

        return out

    def fullPrint(self) -> str:
        out = f'{self.name}:\n'
        for block in self.blocks:
            out += f'{block}\n'

        return out