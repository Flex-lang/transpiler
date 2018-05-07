#! /usr/bin/env python3

'''
The Flex Transpiler.

Usage:
  flex_transpiler <source> -l <lang> [-o <output>]
  flex_transpiler -h

Arguments:
  <source>      Path to the input Flex source file.

Options:
  -l <lang>, --target-language <lang>   The target language to transpile to.
  -o <output>, --output <output>        Path to the generated output file.
  -h, --help                            Print this help text.

Target languages available:
  python
'''

from os import environ
import re

from docopt import docopt
import requests

API_URL = 'https://api.wit.ai/message?v=22/02/2018'
MAIN_REGEX = re.compile(r'Main\(\)\s*')


def generate_code(response, code_dict):
    intent = response['entities']['intent'][0]['value']

    kwargs = {}
    for entity in code_dict[intent]['entities']:
        kwargs[entity] = response['entities'][entity][0]['value']

    return code_dict[intent]['code'].format_map(kwargs) + '\n'


def counts_tabs(line):
    num_tabs = 0
    for character in line:
        if character == '\t':
            num_tabs += 1
        else:
            break
    return num_tabs


if __name__ == '__main__':
    args = docopt(__doc__)
    source_file_path = args['<source>']
    target_language = args['--target-language']
    output_file_path = args['--output']

    headers = { 'Authorization': 'Bearer ' + environ['WIT_AUTH'] }

    if target_language == 'python':
        from languages.python import code_dict
    elif target_language == 'c++':
        from languages.c_plus_plus import code_dict

    code = [code_dict['default_code']]
    current_indent_level = 0
    prev_indent_level = 0
    with open(source_file_path, 'r') as source:
        source_lines = source.readlines()
        for line in source_lines:
            print(line, end='')
            current_indent_level = counts_tabs(line)
            if current_indent_level < prev_indent_level:
                code.append('\t' * current_indent_level + code_dict['end_block'])
            if not line.isspace():  # line is not "blank"
                if MAIN_REGEX.match(line):
                    code.append(code_dict['begin_main'])
                else:
                    params = { 'q': line }
                    response = requests.get(API_URL, params=params, headers=headers).json()
                    code.append('\t' * current_indent_level + generate_code(response=response, code_dict=code_dict))
            prev_indent_level = current_indent_level
    while current_indent_level > 0:
        code.append('\t' * (current_indent_level - 1) + code_dict['end_block'])
        current_indent_level -= 1

    with open(output_file_path, 'w') as output:
        output.writelines(code)
