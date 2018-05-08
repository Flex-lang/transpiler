code_dict = {
    'end_block': '\n',

    'default_code': '',

    'begin_main': '''if __name__ == '__main__':\n''',

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


    #Conditional
    # if
    'begin_if': {
        'entities': ['condition'],
        'code': 'if {condition}:'
    },
    # else
    'begin_else': {
	'entities': [],
        'code': 'else:'
    },
    # else if
    'begin_else_if': {
        'entities': ['condition'],
        'code': 'elif {condition}:'
    },
    # switch
    'begin_switch': {
        'entities': ['switch_var'],
        'code': ''
    },
    # case
    'begin_case': {
        'entities': ['case_value'],
        'code': ''
    },
    # unless
    'begin_unless': {
        'entities': ['condition'],
        'code': 'if not {condition}:'
    },


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

    # Declare variables
    'declare_var': {
        'entities': ['var_name', 'var_type'],
        'code': ''
    },

    'declare_array': {
        'entities': ['var_name', 'var_type'],
        'code': '{var_name} = []'
    },

    # Assignment / initialisation
    'initialize_assign': {
        'entities': ['var_name', 'var_value'],
        'code': '{var_name} = {var_value}'
    },
}
