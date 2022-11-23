import manager
import blocks.blockBuilder as blockBuilder


def main():
    # instantiate the manager -- SHOULD BE A SINGLETON
    m = manager.new()
    # create two routines
    m.create_routine()
    # manager.editRoutine(i) returns the given routine object -- IS THIS OKAY? HOW TO MODIFY ROUTINES IF NOT?
    r = m._get_routine(0)
    # routine modification through method chaining
    r.set_name('Push I').create_block(blockBuilder.new().add_clock(start = 0, end = 15).add_block(weight = 185, sets = 4, reps = 8).build())

    #r.display()
    r.run()

if __name__ == '__main__':
    main()