"""
tools
"""

# forces user to input one of the given switch cases
def safe_input_switch(prompt, options, matches):
    print(prompt)
    print_options(options)

    return safe_input_match(prompt, matches)

# forces user to input something castable to 'type' within range [first, last)
def safe_input_range(prompt, options, type, first, last):
    print_enumerated_options(options)

    i = safe_input_type(prompt, type)
    while i < first or i >= last:
        print(f'{i} is out of range.')
        i = safe_input_type(prompt, type)

    return i

# forces user to input something castable to 'type'
def safe_input(prompt, options, type) -> type:
    print(prompt)
    print_enumerated_options(options)

    return safe_input_type(prompt, type)

# input checking from a list of possible matches
def safe_input_match(prompt, matches):
    user_input = input()
    for match in matches:
        if user_input.lower().strip() == match:
            return match

    print(f'{user_input} is not a valid choice.')
    return safe_input_switch(prompt, matches)
        

# simple type checking of an input with reprompting upon exceptions
def safe_input_type(prompt, type) -> type:
    user_input = input()
    try:
        valid_input = type(user_input)
        return valid_input
    except (ValueError, TypeError):
        print(f'{user_input} is not a valid choice for type {type}.')
        print(prompt)
        return safe_input_type(type)

# display enumerated options from a lists
def print_enumerated_options(options) -> None:
    if options:
        for i, option in enumerate(options):
            print(f'{i}. {option}')

def print_options(options) -> None:
    if options:
        for option in options:
            print(option)