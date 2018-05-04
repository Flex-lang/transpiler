code = {
    # Output
    'print': {
        'entities': ['to_print'],
        'code': 'std::cout << {to_print};'
    },

    
    'print_elements': {
        'entities': ['to_print'],
        'code': '''
            for (const auto& element : {to_print})
    			std::cout << element << ", ";
			std::cout << "\b\b \n";           
        '''
    },

    # Input
    'input': {
        'entities': ['var_name'],
        'code': 'std::cin >> {var_name};'
    },
    # TODO: multiple input

    # Loops
    # for each
    'begin_for_each': {
        'entities': ['loop_over', 'loop_as'],
        'code': 'for(const auto& {loop_as} : {loop_over}) {'
    },
    # while
    'begin_while': {
        'entities': ['condition'],
        'code': 'while({condition}) {'
    },

    # Assignment / initialisation
    'initialize_assign': {
        'entities': ['var_name', 'var_value'],
        'code': '{var_name} = {var_value};'
    },
}
