code_dict = {
    'end_block': '}\n',

    'default_code': '#include <algorithm>\n#include <array>\n#include <cstdlib>\n#include <functional>\n#include <iostream>\n#include <random>\n#include <string>\n#include <vector>\n\n',

    'begin_main': 'int main() {\n',

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


    #Conditional
    # if
    'begin_if': {
        'entities': ['condition'],
        'code': 'if({condition}) {{'
    },
    # else
    'begin_else': {
	'entities': [],
        'code': 'else {{'
    },
    # else if
    'begin_else_if': {
        'entities': ['condition'],
        'code': 'else if ({condition}) {{'
    },
    # switch
    'begin_switch': {
        'entities': ['switch_var'],
        'code': 'switch ({switch_var}) {{'
    },
    # case
    'begin_case': {
        'entities': ['case_value'],
        'code': 'case {case_value} :'
    },
    # unless
    'begin_unless': {
        'entities': ['condition'],
        'code': 'if (!({condition})) {{'
    },


    # Loops
    # for each
    'begin_for_each': {
        'entities': ['loop_over', 'loop_as'],
        'code': 'for (const auto& {loop_as} : {loop_over}) {{'
    },
    # while
    'begin_while': {
        'entities': ['condition'],
        'code': 'while ({condition}) {{'
    },

    # Declare variables
    'declare_var': {
        'entities': ['var_name', 'var_type'],
        'code': '{var_type} {var_name};'
    },
    # TODO
    # 'declare_multi_var': {
    #     'entities': ['var_name', 'var_type'],
    #     'code': '{var_type} ',
    #     'exec': '''
    #         for arg in response['entities']['var_name']:
    #             code += arg['value']
    #         code += ';'
    #     ''',
    # },
    'declare_array': {
        'entities': ['var_name', 'var_type'],
        'code': 'std::vector<{var_type}> {var_name};'
    },

    # Assignment / initialisation
    'initialize_assign': {
        'entities': ['var_name', 'var_value'],
        'code': '{var_name} = {var_value};'
    },
}
