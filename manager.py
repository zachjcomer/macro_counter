import tools
import routine

"""
SINGLETON Manager
Container for routines.
"""

# TODO: not very singleton-y

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

    # self.routines holds all created/saved routines
    def __init__(self):
        self.routines = list()

    def prompt(self):
        options = self.list()
        options.append('Create new routine')

        user_input = tools.safe_input_range('\nSelect a routine:', options, int, 1, len(options) + 1)

        if len(self.routines) > 0:
            if user_input < len(self.routines):
                self._get_routine(user_input).prompt()
            elif user_input == len(self.routines):
                self.create_routine().prompt()
            else:
                print('Goodbye!')
                return
        else:
            if user_input == 0:
                self.create_routine().prompt()
            else:
                print('Goodbye!')
                return 

        self.prompt()

    # create a new routine with a default name
    def create_routine(self):
        r = routine.new(len(self.routines))
        self.routines.append(r)
        return r

    def _get_routine(self, i):
        return self.routines[i]

    # delete a routine
    def delete_routine(self, i):
        self.routines.pop(i)    

    # get safe input for selecting a routine
    def _select_routine(self, prompt):
        return tools.safe_input_range(prompt, self.list(), int, 1, len(self.routines) + 1) - 1

    # return a list of the routines
    def list(self) -> str:
        out = list()
        for r in self.routines:
            out.append(str(r))
        return out

    # pretty print the routines
    def display(self) -> None:
        print('Routines:')
        for i, r in enumerate(self.routines):
            print(f'{i}. {r}')
