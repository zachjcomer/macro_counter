"""
tools for command line input
"""

'''
str prompt - displayed in input()
'''

def safe_input_template(prompt, template):
    '''
    list(tuple(str name, type val, '+'/'-'/'0' range)) template - format to handle action/clock parameters
    '''
    out = dict()
    for tup in template:
        if tup[2] == '+':
            out[tup[0]] = safe_input_min(tup[0], tup[1], 0)
        elif tup[2] == '-':
            out[tup[0]] = safe_input_max(tup[0], tup[1], 0)
        else:
            out[tup[0]] = safe_input(tup[0], tup[1])

    return out

def safe_input_kwargs(prompt, template):
    '''
    list(tuple(str name, type cal)) template - format for general kwargs inputs
    '''
    out = dict()
    for tup in template:
        out[tup[0]] = safe_input_type(tup[0], tup[1])

    return out

def safe_input_switch(prompt, options, matches):
    '''forces user to input one of the given switch cases'''
    print_options(options)

    return safe_input_exact(prompt, matches)

def safe_input_range(prompt, options, type, first, last) -> int:
    '''forces user to input something castable to 'type' within range [first, last)'''
    print_enumerated_options(options)

    i = safe_input_type(prompt, type)
    while i < first or i >= last:
        print(f'{i} is out of range.')
        i = safe_input_range(prompt, options, type, first, last)

    return i

def safe_input(prompt, options, type) -> type:
    '''forces user to input something castable to type'''
    print_enumerated_options(options)

    return safe_input_type(prompt, type)

def safe_input_exact(prompt, matches):
    '''input checking from a list of possible matches'''
    user_input = input(prompt)
    input_formatted = user_input.lower().strip()
    if input_formatted in matches:
        return input_formatted

    print(f'{input_formatted} is not a valid choice.')
    return safe_input_switch(prompt, matches)
        
def safe_input_min(prompt, type, min) -> int:

    user_input = safe_input_type(prompt, type)
    while user_input <= min:
        print(f'{user_input} must be >= {min}.')
        user_input = safe_input_min(prompt, type, min)

    return user_input

def safe_input_max(prompt, type, max) -> int:

    user_input = safe_input_type(prompt, type)
    while user_input >= max:
        print(f'{user_input} must be >= {min}.')
        user_input = safe_input_max(prompt, type, max)

    return user_input

def safe_input_type(prompt, type) -> type:
    '''simple type checking of an input with reprompting upon exceptions'''
    user_input = input(prompt)
    try:
        valid_input = type(user_input)
        return valid_input
    except (ValueError, TypeError):
        print(f'{user_input} is not a valid choice for type {type}.')
        return safe_input_type(prompt, type)

def print_enumerated_options(options) -> None:
    '''display enumerated options from a lists'''
    if options:
        for i, option in enumerate(options):
            print(f'{i + 1}. {option}')

def print_options(options) -> None:
    if options:
        for option in options:
            print(option)