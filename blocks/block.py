import tools
from time import sleep

"""
COMPOSITE Block
* consisting of an Action class and a Clock class.

Implementations I can think of rn: lifting -- (set/rep/weight, cooldown timer), calesthenics -- (set/rep, cooldown), HIIT training -- (interval timer), cardio -- (stopwatch/timer)
"""

def new():
    return Block()

class Block:
    def __init__(self):
        self.name = 'block'
        self.clock = None
        self.action = None

    # executes the block's activity and timer
    def run(self):
        self.action.start()

        while (self.action.is_active()):
            self.clock.start()
            while (self.clock.is_active()):
                sleep(1.0)
                self.clock.tick()
            self.action.end_cycle()

    # set the clock
    def _set_clock(self, clock):
        self.clock = clock

    # set the action
    def _set_action(self, action):
        self.action = action

    # returns block name
    def get_name(self) -> str:
        return self.name

    # sets block name
    def set_name(self, name):
        self.name = name

    def set_name_safe(self, name) -> str:
        name = tools.safeInput(f'Enter new name for {self.get_name()}:', [], str)
        self.name = name

    # pretty print the block's components
    def display(self) -> None:
        print(f'{self.get_name()}')

    # returns the block's name
    def __str__(self) -> str:
        return self.get_name()
