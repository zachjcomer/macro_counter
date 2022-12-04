import blocks.actions.action as action
import tools

class Weight_Lifting(action.Action):

    action_args = [('sets', int, '+'), ('reps', int, '+'), ('weight', float, '+')]
    action_inputs = [('weight', float, '+')]

    def __init__(self, **action_config):
        self.sets = action_config.get('sets')
        self.reps = action_config.get('reps')

        self.data = list()

    def end_cycle(self) -> None:
        self.sets -= 1
        user_input = tools.safe_input_template('Enter:', self.action_inputs)
        self.data.append(user_input['weight'])
        print(f'Sets left: {self.sets}')
        if self.sets == 0:
            self.end()

    def end(self) -> None:
        print(self.data)
        self.active = False

    def set_scheme(self) -> None:
        return super().set_scheme()
        
    def get_inputs() -> list:
        return Weight_Lifting.action_args

    def __str__(self) -> str:
        # return f'{self.sets}x{self.reps} @ {self.weight}'
        return f'{self.sets}x{self.reps}'