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
        self.routines = []

    # creates a new routine and returns it for routine builder
    def runRoutine(self):
        i = self._selectRoutine('Select a routine to run.')        
        self.routines[i].run()

    # create a new routine with a default name
    def createRoutine(self):
        r = routine.new(len(self.routines))
        self.routines.append(r)

    # TODO
    def editRoutine(self):
        i = self._selectRoutine('Select a routine to edit.')
        return self.routines[i]

    # delete a routine
    def deleteRoutine(self):
        i = self._selectRoutine('Select a routine to delete.')
        if tools.safeInputSwitch(f'Are you sure you want to delete {self.routines[i]}?', ['y/n'], ['y', 'n']) == 'y':
            self.routines.pop(i)

    # get safe input for selecting a routine
    def _selectRoutine(self, prompt):
        return tools.safeInputRange(prompt, self.list(), int, 0, len(self.routines))

    # return a list of the routines
    def list(self) -> str:
        out = []
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
    def _getRoutine(self, i):
        return self.routines[i]