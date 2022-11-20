import routine

# ensures that the input is of given type
def safeInput(prompt, options, type) -> type:
    print(f'{prompt}')
    if options:
        for i, option in enumerate(options):
            print(f'{i}. {option}')

    userInput = input()

    try:
        x = type(userInput)
        return x
    except (ValueError, TypeError):
        print(f'{userInput} is not a valid choice for type {type}.')
        return safeInput(prompt, options, type)  

def main():
    routines = []
    routines.append(routine.new())

    r1 = routines[0]
    r1.setName('Push I').addBlock(name = 'Bench Press', reps = 8, sets = 3).addBlock(name = 'Overhead Press', reps = 10, sets = 3).moveBlock(0, 1)

    routineNames = []
    for r in routines:
        routineNames.append(str(r))

    opt = safeInput('Choose routine:', routineNames, int)
    while opt >= len(routines):
        print(f'{opt} is out of range.')
        opt = safeInput('Choose routine:', routineNames, int)

    print(f'Running routine {opt}.')
    print(routines[opt].fullPrint())

if __name__ == '__main__':
    main()