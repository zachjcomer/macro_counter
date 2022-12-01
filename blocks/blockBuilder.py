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

def new():
    return BlockBuilder()

class BlockBuilder():
    # creates new block with dummy clock and action
    def __init__(self):
        self.new_block = block.new()
        self.new_block._set_clock(clock.Clock())
        self.new_block._set_action(action.Action())

    def prompt(self):
        options = ['clock -> timer', 'action -> weight lifting', 'Go back']
        user_input = tools.safe_input_range(f'\n{self}', options, int, 1, len(options) + 1)

        match user_input:
            case 1:
                self.set_timer(**tools.safe_input_kwargs('Configure timer:', timer.Timer.clock_inputs))
            case 2:
                self.set_weight_lifting(**tools.safe_input_kwargs('Configure lift:', weight_lifting.Weight_Lifting.action_inputs))
            case 3:
                return self
        return self.prompt()

    # makes the block a Timer (count down) type
    def set_timer(self, **clock_config):
        self.new_block._set_clock(timer.Timer(**clock_config))
        return self

    # resets the clock to be a dummy clock
    def reset_clock(self):
        self.new_block._set_clock(clock.Clock())
        return self

    def set_weight_lifting(self, **action_config):
        self.new_block._set_action(weight_lifting.Weight_Lifting(**action_config))
        return self

    # resets the action to be a dummy action
    def reset_action(self):
        self.new_block._set_action(action.Action())
        return self

    # resets the block to have a dummy clock and action
    def reset(self):
        self.new_block = block.new()
        self.new_block._set_clock(clock.Clock())
        self.new_block._set_action(action.Action())
        return self

    # give a name to the block
    def name(self, name):
        self.new_block.set_name(name)
        return self

    # complete creation and return the block
    def build(self):
        return self.new_block

    # TODO: I DONT LIKE THIS
    def __str__(self):
        return f'{self.new_block.get_name()}: {self.new_block._get_action().__str__()}, {self.new_block._get_clock().__str__()}'
