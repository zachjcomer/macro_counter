import blocks.clocks.clock as clock

"""
CLOCK Timer
A simple countdown timer. Given an [end_time], counts down from [end_time] to 0 and calls self.end() at that time.
"""

class Timer(clock.Clock):
    """
    Timer clock_config:
    * end_time = lapsed time [s, float] when self.end() is called.
    """
    clock_args = [('end_time', float, '+')]

    def __init__(self, **clock_config):
        self.elapsed_time = 0
        self.end_time = clock_config.get('end_time')

    def tick(self):
        if self.is_active:
            self.elapsed_time += 1
            print(f'timer: {self.end_time - self.elapsed_time}')
            if (self.elapsed_time >= self.end_time):
                self.end()

    def start(self) -> None:
        self.reset()
        self.active = True

    def reset(self) -> None:
        self.elapsed_time = 0

    def get_inputs() -> list:
        return Timer.clock_args
    