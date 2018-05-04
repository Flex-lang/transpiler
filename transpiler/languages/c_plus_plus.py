code = {
    # Output
    'print': {
        'entities': ['to_print'],
        'code': 'cout << {to_print};'
    },

    # TODO: data type to use in looping, by default it's int.
    'print_elements': {
        'entities': ['to_print'],
        'code': '''
            for(const int &element : {to_print})
                cout << element << endl;            
        '''
    },

    # Input
    'input': {
        'entities': ['var_name'],
        'code': 'cin >> {var_name};'
    },
    # TODO: multiple input

    # Loops
    # for each
    # TODO: data type to use in looping, by default it's int.
    'begin_for_each': {
        'entities': ['loop_over', 'loop_as'],
        'code': 'for(int {loop_as} : {loop_over})'
    },
    # while
    'begin_while': {
        'entities': ['condition'],
        'code': 'while({condition})'
    },

    # Assignment / initialisation
    'initialize_assign': {
        'entities': ['var_name', 'var_value'],
        'code': '{var_name} = {var_value};'
    },
}
