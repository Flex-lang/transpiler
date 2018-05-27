code_dict = {
    'end_block': '}\n',

    'default_code': 'import java.awt.*;\nimport java.awt.geom.*;\nimport java.io.*;\nimport java.util.*;\n\n',

    'begin_main': 'public class Test {\npublic static void main() {\n',

    # Output
    'print': {
        'entities': ['to_print'],
        'code': 'System.out.println({to_print});'
    },


    'print_elements': {
        'entities': ['to_print'],
        'code': '''
            for (Object element : {to_print})
                System.out.print(element + ", ");
            System.out.println("\b\b \n");
        '''
    },

    # Input
    # TODO handling different data types
    'input': {
        'entities': ['var_name'],
        'code': '{var_name} = System.console().readLine();'
    },
    # TODO: multiple input


    #Conditional
    # if
    'begin_if': {
        'entities': ['expression'],
        'code': 'if ({expression}) {{'
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
        'code': 'for (Object {loop_as} : {loop_over}) {{'
    },
    # while
    'begin_while': {
        'entities': ['expression'],
        'code': 'while ({expression}) {{'
    },

    # Declare variables
    'declare_var': {
        'entities': ['name', 'type'],
        'code': '{type} {name} = new {type}();'
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
        'code': 'ArrayList<{type}> {name} = new ArrayList<{type}>();'
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
