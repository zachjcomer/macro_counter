import tools
import time

"""
ABSTRACT Clock

Implementations I can think of rn: stopwatch (count up), timer (count down), pacer (HIIT, lift timing, eg fast phase slow phase)
"""
class Clock:
    def __init__(self):
        self.time = 0
        return

    # start the timer's recording
    def start(self):
        print(time.time())
        return

    # pause the timer's recording
    def pause(self):
        return

    # finish the timer's recording, save the data
    def end(self):
        return

    # reset the timer to its initial configuration
    def reset(self):
        return