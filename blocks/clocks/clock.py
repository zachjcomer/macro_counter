"""
INTERFACE Clock

start() the timer's functionality.
pause() the timer in its current state.
end() the timer's functionality.
reset() the timer to its original state.

Implementations I can think of rn: stopwatch (count up), timer (count down, cooldown), pacer (HIIT, lift timing, eg fast phase slow phase), tempo
"""
class Clock:
    def __init__(self, **clock_config):
        self.active = False

    def tick(self) -> None:
        '''called every tick by block.run(), put any time-updating logic here.'''
        print('Error: class Clock is abstract. Please implement in a subclass.')
        self.end()
        return

    def start(self) -> None:
        '''start the timer's recording'''
        self.active = True

    def pause(self) -> None:
        '''pause the timer's recording'''
        self.active = False

    def end(self) -> None:
        '''should be called when the timer successfully reaches its end condition'''
        self.active = False

    def reset(self) -> None:
        '''reset the timer to its initial configuration'''
        return

    def is_active(self) -> bool:
        return self.active

    def __str__(self) -> str:
        return f'clock_generic'
        