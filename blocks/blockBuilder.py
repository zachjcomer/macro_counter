import block
import blocks.clocks.clock as clock
import blocks.actions.action as action

"""
BUILDER BlockBuilder
Handles the creation of a block.
"""

def new():
    return BlockBuilder()

class BlockBuilder():
    def __init__(self):
        self.block_obj = block.new()

    # add a timer to the block
    def add_clock(self, **clock_config):
        self.block_obj.add_clock(clock.Clock(**clock_config))

    # delete the timer from the block
    def delete_clock(self):
        self.block_obj.delete_clock()

    def add_action(self, **action_config):
        self.block_obj.add_action(action.Action(**action_config))

    # restart block creation from a blank block
    def reset(self):
        self.block_obj = block.new()

    # give a name to the block
    def name(self, name):
        self.block_obj.set_name(name)

    # complete creation and return the block
    def build(self):
        return self.block_obj