# The Flex Transpiler

Implementation of Flex's transpiler using the NLU model trained using [Rasa NLU](https://github.com/RasaHQ/rasa_nlu).

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

1. Activate your virtual environment:
   ```bash
   . venv/bin/activate
   ```

1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Train NLU model

From the `transpiler/data` directory, run:

```bash
python -m rasa_nlu.train --config model_config.yml --data intents --path model
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

From the `transpiler` directory, run `flex_transpiler.py` with proper arguments. For example, if your Flex source code is written in `~/input_source.flex` and you want to transpile it to Python into `~/output_source.py`, you need to run the following command:
   ```bash
   ./flex_transpiler.py ~/input_source.flex -l python -o ~/output_source.py
   ```

## License

This project is licensed under the terms of the [MIT license](LICENSE).
