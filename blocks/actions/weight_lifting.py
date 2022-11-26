import blocks.actions.action as action


class Weight_Lifting(action.Action):
    def __init__(self, **action_config):
        self.sets = action_config.get('sets')
        self.reps = action_config.get('reps')
        self.weight = action_config.get('weight')

    def __str__(self):
        return f'{self.sets}x{self.reps} @ {self.weight}'