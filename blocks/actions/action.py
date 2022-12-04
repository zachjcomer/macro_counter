import tools

"""
INTERFACE Action

Implementations I can think of rn: lifting -- sets/reps/weights, bodyweight (calesthentics, etc) -- sets/reps
"""

class Action:
    def __init__(self, **action_config):
        self.active = False
        self.set_scheme()

    def start(self) -> None:
        self.active = True

    def end_cycle(self):
        print('Error: class Action is abstract. Please implement in a subclass.')
        self.end()

    def end(self) -> None:
        self.active = False

    def is_active(self) -> bool:
        return self.active

    def set_scheme(self):
        '''Called from constructor to handle '''
        return

    def get_inputs(self) -> list:
        '''returns the name and type structure of action's data'''
        return list()

    def __str__(self) -> str:
        return 'action_generic'
    