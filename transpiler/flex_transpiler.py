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

from docopt import docopt
import requests

API_URL = 'https://api.wit.ai/message?v=22/02/2018'


def generate_code(response, language):
    intent = response['entities']['intent'][0]['value']
    
    if language == 'python':
        from languages.python import code
    
    kwargs = {}
    for entity in code[intent]['entities']:
        kwargs[entity] = response['entities'][entity][0]['value']
    
    return code[intent]['code'].format_map(kwargs)


if __name__ == '__main__':
    args = docopt(__doc__)
    source_file_path = args['<source>']
    target_language = args['--target-language']
    output_file_path = args['--output']
    
    headers = { 'Authorization': 'Bearer ' + environ['WIT_AUTH'] }
    code = []
    with open(source_file_path, 'r') as source:
        source_lines = source.readlines()
        for line in source_lines:
            if not line.isspace():  # line is not "blank"
                params = { 'q': line }
                response = requests.get(API_URL, params=params, headers=headers).json()
                code.append(generate_code(response=response, language=target_language))

    with open(output_file_path, 'w') as output:
        output.writelines(code)
