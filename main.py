import routine

def run(routines):
    print('Choose routine:')
    for i, routine in enumerate(routines):
        print(f'{i}. {routine.getName()}')

def main():
    routines = []
    routines.append(routine.new())
    r1 = routines[0]
    r1.setName('Push I').addBlock(name = 'Bench Press', reps = 8, sets = 3).addBlock(name = 'Overhead Press', reps = 10, sets = 3)
    r1.moveBlock(0, 1)
    print(r1)

if __name__ == '__main__':
    main()