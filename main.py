import manager
import clock
import routine


def main():
    # instantiate the manager -- SHOULD BE A SINGLETON
    m = manager.new()
    # create two routines
    m.create_routine()
    # manager.editRoutine(i) returns the given routine object -- IS THIS OKAY? HOW TO MODIFY ROUTINES IF NOT?
    r = m._get_routine(0)
    # routine modification through method chaining
    r.set_name('Push I')._create_block(name = 'Overhead Press')._create_block(name = 'Test')
    b = r._get_block(0)
    b._add_clock(clock.Clock())
    b = r._get_block(1)
    b._add_clock(clock.Clock())
    #r.display()
    r.run()

if __name__ == '__main__':
    main()