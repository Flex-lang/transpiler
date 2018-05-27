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
        'entities': ['expression'],
        'code': 'if {expression}:'
    },
    # else
    'begin_else': {
	'entities': [],
        'code': 'else:'
    },
    # else if
    'begin_else_if': {
        'entities': ['expression'],
        'code': 'elif {expression}:'
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
        'entities': ['expression'],
        'code': 'if not {expression}:'
    },


    # Loops
    # for each
    'begin_for_each': {
        'entities': ['loop_over', 'loop_as'],
        'code': 'for {loop_as} in {loop_over}:'
    },
    # while
    'begin_while': {
        'entities': ['expression'],
        'code': 'while {expression}:'
    },

    # Declare variables
    'declare_var': {
        'entities': ['name', 'type'],
        'code': ''
    },

    'declare_array': {
        'entities': ['name', 'type'],
        'code': '{name} = []'
    },

    # Assignment / initialisation
    'assign_variable': {
        'entities': ['name', 'expression'],
        'code': '{name} = {expression}'
    },
    'assign_array': {
        'entities': ['name', 'array_values'],
        'code': '{name} = [ {array_values} ]'
    },
}
