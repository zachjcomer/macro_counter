import tools
import routine

"""
SINGLETON Manager
Container for routines.
"""

# TODO: not very singleton-y

def new():
    return Manager()

class Manager:

    # self.routines holds all created/saved routines
    def __init__(self):
        self.routines = list()

    # creates a new routine and returns it for routine builder
    def run_routine(self):
        i = self._select_routine('Select a routine to run.')        
        self.routines[i].run()

    # create a new routine with a default name
    def create_routine(self):
        r = routine.new(len(self.routines))
        self.routines.append(r)

    # TODO
    def edit_routine(self):
        i = self._select_routine('Select a routine to edit.')
        return self.routines[i]

    # delete a routine
    def delete_routine(self):
        i = self._select_routine('Select a routine to delete.')
        if tools.safe_input_switch(f'Are you sure you want to delete {self.routines[i]}?', ['y/n'], ['y', 'n']) == 'y':
            self.routines.pop(i)

    # get safe input for selecting a routine
    def _select_routine(self, prompt):
        return tools.safe_input_range(prompt, self.list(), int, 0, len(self.routines))

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

    """UNSAFE METHODS BELOW THIS LINE -- USE WITH CAUTION -- DONT PERFORM INPUT VALIDATION OR RANGE CHECKING"""
    # bad?, need to find a way to edit/build routines through manager or in a more "managed" way
    def _get_routine(self, i):
        return self.routines[i]
