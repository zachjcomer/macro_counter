import tools
import blocks.block as block
import blocks.clocks.clock as clock
import blocks.clocks.timer as timer
import blocks.actions.action as action
import blocks.actions.weight_lifting as weight_lifting

"""
BUILDER BlockBuilder
Handles the creation of a block.
"""

class BlockBuilder():
    def __init__(self):
        '''creates new block with dummy clock and action'''
        self.new_block = block.Block()
        self.new_block._set_clock(clock.Clock())
        self.new_block._set_action(action.Action())

    def prompt(self):
        options = ['clock -> timer', 'action -> weight lifting', 'Go back']
        user_input = tools.safe_input_range(f'{self}', options, int, 1, len(options) + 1)

        match user_input:
            case 1:
                self.set_timer(**tools.safe_input_template('Configure timer:', timer.Timer.get_inputs()))
            case 2:
                self.set_weight_lifting(**tools.safe_input_template('Configure lift:', weight_lifting.Weight_Lifting.get_inputs()))
            case 3:
                return self
        return self.prompt()

    def set_timer(self, **clock_config):
        '''adds timer (count down) functionality'''
        self.new_block._set_clock(timer.Timer(**clock_config))
        return self

    def reset_clock(self):
        '''resets the clock type to be a dummy clock'''
        self.new_block._set_clock(clock.Clock())
        return self

    def set_weight_lifting(self, **action_config):
        '''adds weight lifting functionality'''
        self.new_block._set_action(weight_lifting.Weight_Lifting(**action_config))
        return self

    def reset_action(self):
        '''resets the action type to be a dummy action'''
        self.new_block._set_action(action.Action())
        return self

    def reset(self):
        '''resets the block to have a dummy clock and action type'''
        self.new_block = block.new()
        self.new_block._set_clock(clock.Clock())
        self.new_block._set_action(action.Action())
        return self

    def name(self, name):
        '''give a name to the block'''
        self.new_block.set_name(name)
        return self

    def build(self):
        '''complete creation and return the block'''
        return self.new_block

    # TODO: I DONT LIKE THIS
    def __str__(self):
        return f'{self.new_block.get_name()}: {self.new_block._get_action().__str__()}, {self.new_block._get_clock().__str__()}'
