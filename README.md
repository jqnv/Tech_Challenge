# Tech Challenge

Python app to obtain stats from a list of integers provided

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install podcast_api.

```bash
pip install virtualenv
pip install pytest
```

## Usage

```python
import pytest

class DataCapture: # class which Gather a list of integers from a user input 
                   # and also the parameters to get the stats. 
def add(): # Get the numbers from a user input request to be evaluated
def get_param() # The user will determine the value of any parameter to get the stats
def build_stats() # Contains the functions to get any parameter requested
    def less() # Determine how many numbers on the list are less than the parameter provided for the less than stat
    def between() # Determine how many numbers on the list are between the numbers entered as parameters provided for the between stat
    def greater() # Determine how many numbers on the list are greater than the parameter provided for the greater than stat
    # Note: before pass the ordered list to the greater method it is inverted in order to optimize the process speed

# At the end is presented on the screen the list as was entered and
# the result for every stat required.

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[Joaquin Vasquez](https://github.com/jqnv/)