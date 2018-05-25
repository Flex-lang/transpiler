# The Flex Transpiler: Wit edition

Implementation of Flex's transpiler using the NLU model trained on [Wit.ai](https://wit.ai).

## Setup

1. Clone the repo and **`cd`** into it:
   ```bash
   git clone https://github.com/Flex-lang/transpiler-wit.git
   cd transpiler-wit
   ```

1. Create a Python 3 virtual environment (named `venv`):
   ```bash
   virtualenv -p python3 venv
   ```

1. Add Wit's API _"Server Access Token"_ as an environment variable. For ease, add it to your virtual environment's activate script:
   ```bash
   printf "\nexport WIT_AUTH='enter your token here'\n" >> venv/bin/activate
   ```

1. Activate your virtual environment:
   ```bash
   . venv/bin/activate
   ```

1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Run

```
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
  c++
  java
  python
```

0. Make sure your virtual environment is activated.

1. **`cd`** into the `transpiler` directory and run `flex_transpiler.py` with proper arguments. For example, if your Flex source code is written in `~/input_source.flex` and you want to transpile it to Python into `~/output_source.py`, you need to run the following command:
   ```bash
   ./flex_transpiler.py ~/input_source.flex -l python -o ~/output_source.py
   ```

## License

This project is licensed under the terms of the [MIT license](LICENSE).
