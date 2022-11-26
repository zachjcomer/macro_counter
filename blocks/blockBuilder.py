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