import tools
import manager
import blocks.blockBuilder as blockBuilder

def main():
    # instantiate the manager -- SHOULD BE A SINGLETON
    m = manager.new()
    m.create_routine()
    # opt = tools.safe_input_range('Pick an option', ['Create a routine.'], int, 0, 1)
    m.prompt()

    """ # create two routines
    
    # manager.editRoutine(i) returns the given routine object -- IS THIS OKAY? HOW TO MODIFY ROUTINES IF NOT?
    r = m._get_routine(0)
    # routine modification through method chaining
    r.set_name('Push I').create_block(blockBuilder.new().set_timer(time = 5).set_weight_lifting(sets = 4, reps = 10).build())

    #r.display()
    r.run() """
    
if __name__ == '__main__':
    main()
