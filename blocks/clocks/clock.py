import tools
import time

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
        self.start_time = clock_config.get('start_time', 0)

    # start the timer's recording
    def start(self):
        print(time.time())

    # pause the timer's recording
    def pause(self):
        return

    # finish the timer's recording, save the data
    def end(self):
        return

    # reset the timer to its initial configuration
    def reset(self):
        return

    def __str__(self):
        return f'{self.start_time}'