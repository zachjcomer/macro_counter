class Block:
    def __init__(self, i):
        self.name = f'Block{i}'

    def getName(self):
        return self.name

    def setName(self, newName):
        if (isinstance(newName, str)):
            print(f'Naming block {self.name} to {newName}')
            self.name = newName
        else:
            print(f'Error: Block#setName requires str but {type(newName).__name__} was supplied.')
        return self

    def run(self):
        print(f'Do block {self.name}')
        input()