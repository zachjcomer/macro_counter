def new(**blockConfig):
    return Block(**blockConfig)

class Block:
    def __init__(self, **blockConfig):
        for option, value in blockConfig.items():
            if isinstance(option, str) and option.lower().strip() == "name":
                if isinstance(value, str):
                    self.name = f'{value}'
            if isinstance(option, str) and option.lower().strip() == "sets":
                if isinstance(value, int):
                    self.sets = value
            if isinstance(option, str) and option.lower().strip() == "reps":
                if isinstance(value, int):
                    self.reps = value


    def getName(self):
        return self.name

    def setName(self, newName):
        if (isinstance(newName, str)):
            # print(f'Naming block {self.name} to {newName}')
            self.name = newName
        else:
            print(f'Error: Block#setName requires str but {type(newName).__name__} was supplied.')
        return self

    def __str__(self) -> str:
        return f'{self.name}: {self.sets} x {self.reps}'

    def run(self):
        print(f'Do block {self.name}')
        input()