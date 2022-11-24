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
        self.is_active = False

    # start the timer's recording
    def start(self):
        self.is_active = True

    # pause the timer's recording
    def pause(self):
        self.is_active = False
        return

    # called every tick by block.run(), put any time-updating logic here.
    def tick(self):
        if self.is_active:
            return

    # should be called when the timer successfully reaches its end condition
    def end(self):
        return

    # reset the timer to its initial configuration
    def reset(self):
        return

    def __str__(self):
        return f'{self.start_time}'