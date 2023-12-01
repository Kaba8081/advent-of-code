# advent-of-code
![](https://img.shields.io/badge/stars%20⭐-2-yellow)
![](https://img.shields.io/badge/days%20completed-1-red)
## Overwiew
This repository contains my sollutions to a series of programming challanges called [Advent of code](https://adventofcode.com/).

## input-grabber.py
To skip the hustle of making a new directory every time i want to move on to the next problem, I've created this simple program that creates a new directory and grabs a specified input file directly from AOC website. 

### Flags
By default the program will try to get the problem's input based on the current date, but it can also be specified by supplying these paremeters in the console window:

- `-y` or `--year` \
  **Default**: current year \
  specify desired year of the challange (>=2015)
- `-d` or `--day` \
  **default**: current day \
  specify desired day of the challange (between 1 - 25)
- `-c` or `--create` \
  **default**: False \
  When set to `True` creates a `main.py` file inside the `./year/day/` directory with the following contents:
  ```python3
  # 'Advent of code' solution for year {0} day {1}
  import os
  import sys
       
  dir_path = os.path.dirname(os.path.realpath(__file__))
  input = None
  
  with open(os.path.join(dir_path, "input.txt"), "r") as file:    
      input = file.read().strip().splitlines()
  if not input:
      print("Error! Input file is empty!")
      sys.exit()
                          
  if __name__ == "__main__":
      sys.exit()
  ```

### AOC_COOKIE
Advent of code's input files are generated based on the user's id inside the browser cookies, so in order to retrieve the input file from the server this variable needs to be specified in a new file called `.env`.
Inside this file should be a line of code that looks like this:
```python3
AOC_COOKIE = "..." # secret cookie id goes here
```