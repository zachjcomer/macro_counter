import manager
import routine

def main():
    m = manager.new()
    m.createRoutine()
    m.createRoutine()
    r = m._editRoutine(0)
    r.setName('Push I').createBlock(name = 'Bench Press', reps = 8, sets = 3).createBlock(name = 'Overhead Press', reps = 10, sets = 3).moveBlock(0, 1)

    print(r.list())
    r.deleteBlock()
    print(r.list())

if __name__ == '__main__':
    main()