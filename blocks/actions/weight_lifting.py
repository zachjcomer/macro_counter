import blocks.actions.action as action


class Weight_Lifting(action.Action):

    action_args = [('sets', int, '+'), ('reps', int, '+')]
    action_inputs = [('weight', float, '+')]

    def __init__(self, **action_config):
        self.sets = action_config.get('sets')
        self.reps = action_config.get('reps')
        self.data = None

        self.set_scheme()

    def end_cycle(self) -> None:
        self.sets -= 1
        print(f'Sets left: {self.sets}')
        if self.sets == 0:
            self.end()

    def set_scheme(self) -> None:
        return super().set_scheme()
        
    def get_inputs() -> list:
        return Weight_Lifting.action_args

    def __str__(self) -> str:
        # return f'{self.sets}x{self.reps} @ {self.weight}'
        return f'{self.sets}x{self.reps}'