import tools

"""
INTERFACE Action

Implementations I can think of rn: lifting -- sets/reps/weights, bodyweight (calesthentics, etc) -- sets/reps
"""

# TODO: scheme and data should be coupled?

class Action:
    def __init__(self, **action_config):
        self.data = list() # LIST OF TUPLES OF FLOATS?
        self.scheme = tuple() # TUPLE OF STRINGS?

    def request_input(self):
        i = tools.safeInput(f'Enter data for {self.get_name()}:', self.scheme[0], int)

    """UNSAFE METHODS BELOW THIS LINE -- USE WITH CAUTION -- DONT PERFORM INPUT VALIDATION OR RANGE CHECKING"""
    def _get_data(self, i) -> tuple:
        return self.data[i]

    def _add_data(self, data):
        self.data.append(data)

    def _delete_data(self, i):
        self.data.pop(i)

    def _set_scheme(self, vals):
        self.scheme = tuple(vals)
    
    def _get_scheme(self) -> list:
        return list(self.scheme)