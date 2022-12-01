"""
tools
"""

def safe_input_kwargs(prompt, template):
    out = dict()
    for tup in template:
        if tup[2] == '+':
            out[tup[0]] = safe_input_min(tup[0], tup[1], 0)
        if tup[2] == '-':
            out[tup[0]] = safe_input_max(tup[0], tup[1], 0)

    return out

# forces user to input one of the given switch cases
def safe_input_switch(prompt, options, matches):
    print(prompt)
    print_options(options)

    return safe_input_match(prompt, matches)

# forces user to input something castable to 'type' within range [first, last)
def safe_input_range(prompt, options, type, first, last) -> int:
    print(prompt)
    print_enumerated_options(options)

    i = safe_input_type(prompt, type)
    while i < first or i >= last:
        print(f'{i} is out of range.')
        i = safe_input_range(prompt, options, type, first, last)

    return i

# forces user to input something castable to 'type'
def safe_input(prompt, options, type) -> type:
    print(prompt)
    print_enumerated_options(options)

    return safe_input_type(prompt, type)

# input checking from a list of possible matches
def safe_input_match(prompt, matches):
    user_input = input()
    input_formatted = user_input.lower().strip()
    if input_formatted in matches:
        return input_formatted

    print(f'{input_formatted} is not a valid choice.')
    return safe_input_switch(prompt, matches)
        
def safe_input_min(prompt, type, min) -> int:
    print(prompt)

    i = safe_input_type(prompt, type)
    while i <= min:
        print(f'{i} must be >= {min}.')
        i = safe_input_min(prompt, type, min)

    return i

def safe_input_max(prompt, type, max) -> int:
    print(prompt)

    i = safe_input_type(prompt, type)
    while i >= max:
        print(f'{i} must be >= {min}.')
        i = safe_input_max(prompt, type, max)

    return i

# simple type checking of an input with reprompting upon exceptions
def safe_input_type(prompt, type) -> type:
    user_input = input()
    try:
        valid_input = type(user_input)
        return valid_input
    except (ValueError, TypeError):
        print(f'{user_input} is not a valid choice for type {type}.')
        print(prompt)
        return safe_input_type(prompt, type)

# display enumerated options from a lists
def print_enumerated_options(options) -> None:
    if options:
        for i, option in enumerate(options):
            print(f'{i + 1}. {option}')

def print_options(options) -> None:
    if options:
        for option in options:
            print(option)