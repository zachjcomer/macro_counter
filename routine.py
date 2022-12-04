import tools
import blocks.blockBuilder as blockBuilder

"""
Routine
Container for blocks.
"""

def new(i):
    return Routine(i)

class Routine:
    def __init__(self, i):
        self.name = f'Routine {i}'
        self.blocks = list()

    def prompt(self) -> None:
        options = ['Run', 'Edit', 'Delete', 'Go back']

        user_input = tools.safe_input_range(f'{self} options:', options, int, 1, 5)

        match user_input:
            case 1:
                self.run()
            case 2:
                self.editor()
            case 3:
                print(f'delete {self} [WIP]')
            case 4:
                return # if chosen, returns to manager object, won't run self.prompt() again

        self.prompt()

    def editor(self) -> None:
        options = ['Create new block']
        options = self.list() + options
        
        user_input = tools.safe_input_range(f'{self} editor:', options, int, 1, len(options) + 1)

        if user_input == len(options):
            self.create_block(blockBuilder.BlockBuilder().prompt().build())

    def run(self) -> None:
        '''executes the routine's blocks in order of list appearance'''
        print(f'\nRunning {self.get_name()}.')
        for block in self.blocks:
            block.run()

    def get_name(self) -> str:
        '''returns routine name'''
        return self.name

    def set_name(self, argName):
        '''prompts for a new name'''
        if not argName:
            argName = tools.safeInput(f'Enter a new name for {self.get_name()}.', [], str)
        self.name = argName
        return self

    # what would need a block outside of a routine? a routine is just a block container -- copying routines maybe?
    def get_block(self):
        i = self._select_block(f'Select a block to modify from {self.get_name()}')
        return self.blocks[i]

    def create_block(self, block):
        '''creates a block object with the given blockConfig and adds it to self.blocks'''
        self.blocks.append(block)
        return self

    def delete_block(self):
        '''removes the block from self.blocks if valid'''
        i = self._select_block(f'Select a block to delete from {self.get_name()}')
        if tools.safeInputSwitch(f'Are you sure you want to delete {self.blocks[i]}?', ['y/n'], ['y', 'n']) == 'y':
            self.blocks.pop(i)

    def move_block(self):
        '''swaps blocks at index i,j if possible'''
        i = self._select_block(f'Select the first block to swap from {self.get_name()}')
        j = self._select_block(f'Select the second block to swap from {self.get_name()}')
        self.blocks[i], self.blocks[j] = self.blocks[j], self.blocks[i]

    def display(self) -> None:
        '''pretty print the routine's blocks'''
        print(f'{self.get_name()} blocks:')
        for i, b in enumerate(self.blocks):
            print(f'{i}. {b}')

    def list(self) -> list:
        '''returns a list of the routine's blocks'''
        out = list()
        for block in self.blocks:
            out.append(str(block))
        return out

    def _select_block(self, prompt) -> int:
        '''get safe input for selecting a block'''
        return tools.safeInputRange(f'{prompt}', self.list(), int, 0, len(self.blocks))

    def __str__(self) -> str:
        '''returns the routine's name'''
        return self.get_name()
