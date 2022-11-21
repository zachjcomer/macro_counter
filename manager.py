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

    # TODO
    def editRoutine(self):
        i = self._selectRoutine('Select a routine to edit.')
        return self.routines[i]

    # bad, need to find a way to edit/build routines through manager or in a more "managed" way
    def _editRoutine(self, i):
        return self.routines[i]

    # create a new routine with a default name
    def createRoutine(self):
        r = routine.new(len(self.routines))
        self.routines.append(r)

    # delete a routine
    def deleteRoutine(self):
        i = self._selectRoutine('Select a routine to delete.')
        if tools.safeInputSwitch(f'Are you sure you want to delete {self.routines[i]}?', ['y/n'], ['y', 'n']) == 'y':
            self.routines.pop(i)

    # get safe input for selecting a routine
    def _selectRoutine(self, prompt):
        return tools.safeInputRange(prompt, self.list(), int, 0, len(self.routines))

    # list the routines
    def list(self):
        out = []
        for r in self.routines:
            out.append(str(r))
        return out



