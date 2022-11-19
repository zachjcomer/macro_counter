import block

class Routine:
    def __init__(self):
        self.name = 'Routine'
        self.blocks = [ ]

    def getName(self):
        # returns str self.name
        return self.name

    def setName(self, newName):
        # attempts to replace self.name with newName.
        # returns self for method chaining.
        if isinstance(newName, str):
            print(f'Naming {self.name} to {newName}.')
            self.name = newName
        else:
            print(f'Error: Routine#setName requires str but {type(newName).__name__} was supplied.')
        return self

    def addBlock(self):
        self.blocks.append(block.Block(len(self.blocks)))

    def delBlock(self, i):
        if i < len(self.blocks):
            self.blocks.pop(i)

    def moveBlock(self, i, j):
        # swaps blocks at index i,j if possible
        if i < len(self.blocks) and j < len(self.blocks):
            self.blocks[i], self.blocks[j] = self.blocks[j], self.blocks[i]

    def run(self):
        print(f'Running {self.name}...')
        for block in self.blocks:
            block.run()
