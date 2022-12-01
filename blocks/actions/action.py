import tools

"""
INTERFACE Action

Implementations I can think of rn: lifting -- sets/reps/weights, bodyweight (calesthentics, etc) -- sets/reps
"""

# TODO: scheme and data should be coupled?

class Action:
    def __init__(self, **action_config):
        self.active = False

    def start(self):
        self.active = True

    def end_cycle(self):
        print('Error: class Action is abstract. Please implement in a subclass.')
        self.end()

    def end(self):
        self.active = False

    def is_active(self):
        return self.active

    def __str__(self):
        return 'action_generic'
    