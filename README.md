# advent-of-code
![](https://img.shields.io/badge/days%20completed-3-red)
![](https://img.shields.io/badge/stars%20⭐-7-yellow)
## Overwiew
This repository contains my sollutions in Python to a series of programming challanges called [Advent of code](https://adventofcode.com/).

## input-grabber.py
To skip the hustle of making a new directory every time i want to move on to the next problem, I've created this simple program that automates that process and grabs the specified input file directly from AOC website. 

### Flags
By default the program will try to get the problem's input based on the current date, but it can also be specified by changing some of these paremeters in the console window:

- `-y` or `--year` \
  **Default**: current year \
  specify desired year of the challange (>=2015)
- `-d` or `--day` \
  **Default**: current day \
  specify desired day of the challange (between 1 - 25)
- `-c` or `--create` \
  **Default**: False \
  When set to `True` creates a `main.py` file inside the `./year/day/` directory with the following contents: 
  ```python3
  # 'Advent of code' solution for year {YEAR} day {DAY}
  import os
  import sys
                          
  global DIR_PATH
  DIR_PATH = os.path.dirname(os.path.realpath(__file__))

  def get_input():
      input = None
      if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
          with open(os.path.join(DIR_PATH, "input.txt"), "r") as file:    
              input = file.read().strip().splitlines()
          return input
      else:
          print("Error! Input file does not exist!")
          sys.exit()
                          
  if __name__ == "__main__":
      input = get_input()
      if not input:
          print("Error! Input file is empty!")
          sys.exit()
                          
      # your code goes here
      
      sys.exit()
  ```

### AOC_COOKIE
Advent of code's input files are generated based on the user's id inside the browser cookies. In order to retrieve this file from the server, a variable needs to be specified in a new file called `.env` so that inside it should look like this:
```python3
AOC_COOKIE = "..." # secret cookie id goes here
```
To find the value, press F12 while logged in on [https://adventofcode.com/](https://adventofcode.com/), go to `storage` tab and copy the `session` cookie value. 
