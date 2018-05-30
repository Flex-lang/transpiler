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

1. Install the required libraries:
   ```bash
   pip install rasa_core rasa_nlu[spacy]
   ```

1. Download spAcy model:
   ```bash
   python -m spacy download en_core_web_md
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

## Results

##### Input Flex Code
```bash
Main()
    arr is an array of integers
    x is integer
    input 10 elements in arr
    input x
    flag: boolean
    flag is false
    for every element in arr
   	 if element == x
   		 display "FOUND!"
   		 flag is true
    if flag == false
   	 display "NOT FOUND!"
```

##### Transpiled Python Code
```bash
if __name__ == '__main__':
    input(x)
    value_list = [1, 5, 8, 6, 0, 4, 5]
    print(x)
    for element in value_list:
   	 element = x * element
   	 print(element)
```

##### Transpiled CPP Code
```bash
#include <algorithm>
#include <array>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <random>
#include <string>
#include <vector>

typedef int integer;
typedef float real;
typedef char character;
typedef bool boolean;

int main() {
    std::vector<integer> arr;
    integer x;
    for (size_t i = 0; i < 10; i++) {
   	 integer temp;
   	 std::cin >> temp;
   	 arr.push_back(temp);
    }
    std::cin >> x;
    boolean flag;
    flag = false;
    for (const auto& element : arr) {
   	 If (element == x) {
   		 std::cout << "found!";
   		 flag = true;
    }
    if (flag == false) {
   	 std::cout << "not found!";
    }

    return 0;
}
```

##### Transpiled Java Code
```bash
import java.awt.*;
import java.awt.geom.*;
import java.io.*;
import java.util.*;

public class test {
    public static void main() {
   	 ArrayList<integer> arr = new ArrayList<integer>();
   	 integer x = new integer();
   	 String arr = System.console().readLine();
   	 String x = System.console().readLine();
   	 boolean flag = new boolean();
   	 flag = false;
   	 for (Object element : arr) {
   		 if(element == x) {
   			 System.out.println("found!");
   			 flag = true;
   	 }
   	 If (flag == false) {
   		 System.out.println("not found!");
   	 }
    }
}
```
   
## License

This project is licensed under the terms of the [MIT license](LICENSE).
