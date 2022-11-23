# forces user to input something castable to 'type'
def safe_input(prompt, options, type) -> type:
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
        return safe_input(prompt, options, type)

# forces user to input one of the given switch cases
def safe_input_switch(prompt, options, cases):
    print(f'{prompt}')
    for option in options:
        print(option)

    userInput = input()

    for case in cases:
        if userInput.lower().strip() == case:
            return case

    print(f'{userInput} is not a valid choice.')
    return safe_input_switch(prompt, options, cases)

# forces user to input something castable to 'type' within range [first, last)
# HOW WILL THIS HANDLE NON-NUMERIC OBJECTS?
def safe_input_range(prompt, options, type, first, last):
    i = safe_input(prompt, options, type)
    while i < first or i >= last:
        print(f'{i} is out of range.')
        i = safe_input(prompt, options, type)
    return i