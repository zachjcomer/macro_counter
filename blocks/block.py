import tools
from time import sleep

"""
COMPOSITE Block
* consisting of an Action class and a Clock class.

Implementations I can think of rn: lifting -- (set/rep/weight, cooldown timer), calesthenics -- (set/rep, cooldown), HIIT training -- (interval timer), cardio -- (stopwatch/timer)
"""

class Block:
    def __init__(self):
        self.name = 'block'
        self.clock = None
        self.action = None

    def run(self):
        '''executes the block's activity and timer'''
        self.action.start()

        while (self.action.is_active()):
            self.clock.start()
            while (self.clock.is_active()):
                sleep(1.0)
                self.clock.tick()
            self.action.end_cycle()

    def _get_clock(self):
        return self.clock

    def _set_clock(self, clock):
        '''set the clock implementation'''
        self.clock = clock

    def _get_action(self):
        return self.action

    def _set_action(self, action):
        '''set the action implementation'''
        self.action = action

    def get_name(self) -> str:
        '''returns block name'''
        return self.name

    def set_name(self, name):
        '''sets block name'''
        self.name = name

    def set_name_safe(self, name) -> str:
        name = tools.safeInput(f'Enter new name for {self.get_name()}:', [], str)
        self.name = name

    def display(self) -> None:
        '''pretty print the block's components'''
        print(f'{self.get_name()}')

    def __str__(self) -> str:
        '''returns the block's name'''
        return self.get_name()
