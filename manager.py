import tools
import routine

"""
SINGLETON Manager
Container for routines.
"""

# TODO: not very singleton-y
# TODO: terminate option in #prompt()

"""
Example of input prompt:

Select a routine:
1. {routine[0]}
2. {routine[1]}
3. Create new routine

{routine} options:
1. Run
2. Edit
3. Delete
4. Back

Choose a block to edit:
1. {block[0]}
2. {block[1]}
3. Back

{block[i]} options:
1. Rename {block[i]}
2. Edit Action
3. Edit Clock
4. Back

{action} options:
1. Change params
2. Change action
3. Back

{clock} options:
1. Change params
2. Change action
3. Back

"""

def new():
    return Manager()

class Manager:

    def __init__(self):
        self.routines = list()

    def prompt(self) -> None:
        options = self.list()
        options.append('Create new routine')
        options.append('Exit')

        user_input = tools.safe_input_range('Select a routine:', options, int, 1, len(options) + 1)

        if user_input <= len(self.routines):
            self._get_routine(user_input).prompt()
        elif user_input == len(self.routines) + 1:
            self.create_routine().prompt()
        else:
            print('Goodbye!')
            return

        self.prompt()

    def create_routine(self) -> routine:
        '''create a new routine with a default name'''
        r = routine.new(len(self.routines))
        self.routines.append(r)
        return r

    def _get_routine(self, i) -> routine:
        return self.routines[i]

    def delete_routine(self, i) -> None:
        '''delete a routine'''
        self.routines.pop(i)    

    def _select_routine(self, prompt) -> int:
        '''get safe input for selecting a routine'''
        return tools.safe_input_range(prompt, self.list(), int, 1, len(self.routines) + 1) - 1

    def list(self) -> str:
        '''return a list of the routines'''
        out = list()
        for r in self.routines:
            out.append(str(r))
        return out

    def display(self) -> None:
        '''pretty print the routines'''
        print('Routines:')
        for i, r in enumerate(self.routines):
            print(f'{i}. {r}')
