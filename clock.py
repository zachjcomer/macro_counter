import tools
import time

"""
INTERFACE Clock

start() the timer's functionality.
pause() the timer in its current state.
end() the timer's functionality.
reset() the timer to its original state.

Implementations I can think of rn: stopwatch (count up), timer (count down, cooldown), pacer (HIIT, lift timing, eg fast phase slow phase)
"""
class Clock:
    def __init__(self):
        self.time = 0

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