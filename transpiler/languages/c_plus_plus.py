code_dict = {
    'end_block': '}\n',

    'default_code': '#include <algorithm>\n#include <array>\n#include <cstdlib>\n#include <functional>\n#include <iostream>\n#include <random>\n#include <string>\n#include <vector>\n\ntypedef int integer;\ntypedef float real;\ntypedef string str;\ntypedef char character;\ntypedef bool boolean;\n\n',

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


    # Conditional
    # if
    'begin_if': {
        'entities': ['expression'],
        'code': 'if({expression}) {{'
    },
    # else
    'begin_else': {
	'entities': [],
        'code': 'else {{'
    },
    # else if
    'begin_else_if': {
        'entities': ['expression'],
        'code': 'else if ({expression}) {{'
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
        'entities': ['expression'],
        'code': 'if (!({expression})) {{'
    },


    # Loops
    # for each
    'begin_for_each': {
        'entities': ['loop_over', 'loop_as'],
        'code': 'for (const auto& {loop_as} : {loop_over}) {{'
    },
    # while
    'begin_while': {
        'entities': ['expression'],
        'code': 'while ({expression}) {{'
    },

    # Declare variables
    'declare_var': {
        'entities': ['name', 'type'],
        'code': '{type} {name};'
    },
    # TODO
    # 'declare_multi_var': {
    #     'entities': ['name', 'type'],
    #     'code': '{type} ',
    #     'exec': '''
    #         for arg in response['entities']['name']:
    #             code += arg['value']
    #         code += ';'
    #     ''',
    # },
    'declare_array': {
        'entities': ['name', 'type'],
        'code': 'std::vector<{type}> {name};'
    },

    # Assignment / initialisation
    'assign_variable': {
        'entities': ['name', 'expression'],
        'code': '{name} = {expression};'
    },
    'assign_array': {
        'entities': ['name', 'array_values'],
        'code': '{name} = {{ {array_values} }};'
    },
}
