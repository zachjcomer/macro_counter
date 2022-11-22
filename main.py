import manager
import clock
import routine


def main():
    # instantiate the manager -- SHOULD BE A SINGLETON
    m = manager.new()
    # create two routines
    m.createRoutine()
    # manager.editRoutine(i) returns the given routine object -- IS THIS OKAY? HOW TO MODIFY ROUTINES IF NOT?
    r = m._getRoutine(0)
    # routine modification through method chaining
    r.setName('Push I').createBlock(name = 'Overhead Press', reps = 10, sets = 3).createBlock(name = 'Test')
    b = r._getBlock(0)
    b._addClock(clock.Clock())
    b.run()

if __name__ == '__main__':
    main()