code = {
    # Output
    'print': {
        'entities': ['to_print'],
        'code': 'print({to_print})'
    },
    'print_elements': {
        'entities': ['to_print'],
        'code': '''
            for element in {to_print}:
                print(element, end=', ')
            print('\b\b ')
        '''
    },

    # Input
    'input': {
        'entities': ['var_name'],
        'code': 'input({var_name})'
    },
    # TODO: multiple input

    # Loops
    # for each
    'begin_for_each': {
        'entities': ['loop_over', 'loop_as'],
        'code': 'for {loop_as} in {loop_over}:'
    },
    # while
    'begin_while': {
        'entities': ['condition'],
        'code': 'while {condition}:'
    },

    # Assignment / initialisation
    'initialize_assign': {
        'entities': ['var_name', 'var_value'],
        'code': '{var_name} = {var_value}'
    },
}
