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

    # called every tick by block.run(), put any time-updating logic here.
    def tick(self):
        print('Error: class Clock is abstract. Please implement in a subclass.')
        self.end()
        return

    # start the timer's recording
    def start(self):
        self.active = True

    # pause the timer's recording
    def pause(self):
        self.active = False

    # should be called when the timer successfully reaches its end condition
    def end(self):
        self.active = False

    # reset the timer to its initial configuration
    def reset(self):
        return

    def is_active(self) -> bool:
        return self.active

    def __str__(self) -> str:
        return f'clock_generic'
        