import requests
import argparse
import sys
import os

from datetime import datetime
from dotenv import load_dotenv

def configure():
    load_dotenv()
    
    global AOC_COOKIE, INPUT_URL

    AOC_COOKIE = os.getenv("AOC_COOKIE")
    INPUT_URL = "https://adventofcode.com/{0}/day/{1}/input"


def grab_input(dir_path, year, day, create_file):
    day_path = os.path.join(os.path.join(dir_path, str(year)), str(day))

    print("Grabbing input for year {0} day {1}...".format(year, day))
    res = requests.get(INPUT_URL.format(year, day), cookies=cookies, headers={})

    if res.status_code == 200:
        # create directiories if they don't exist
        if not os.path.exists(os.path.join(dir_path, str(year))):
            os.mkdir(os.path.join(dir_path, str(year)))
        if not os.path.exists(day_path):
            os.mkdir(day_path)
        
        # save the collected text
        with open(os.path.join(day_path, "input.txt"), "w") as f:
            f.write(res.text)

        # create main.py file if requested
        if create_file:
            with open(os.path.join(day_path, "main.py"), "w") as f:
                f.write("""# 'Advent of code' solution for year {0} day {1}
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
""".format(year, day))
        print("Success! Input saved to {0}".format(os.path.join(day_path, "input.txt")))
    else:
        with open(os.path.join(dir_path, "error.log"), "w") as f:
            f.write(f"{res.status_code}\n{res.text}")
        print("Error! Status code: {0}, text: '{1}'\nLog file created in {2}".format(res.status_code, res.text, os.path.join(dir_path, "error.log")))

if __name__ == "__main__":
    configure()
    
    parser = argparse.ArgumentParser(description='Grab input for Advent of Code')
    parser.add_argument('-y', '--year', type=int, help='Year of the event', default=datetime.now().year)
    parser.add_argument('-d', '--day', type=int, help='Day of the event', default=datetime.now().day)
    parser.add_argument('-c', '--create', type=bool, help='Create a "main.py" file inside the input directory', default=False)

    args = parser.parse_args()

    selected_year = args.year
    selected_day = args.day
    create_file = args.create

    cookies = {"session":AOC_COOKIE}
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if selected_year < 2015 or selected_year > datetime.now().year:
        print("Invalid year! Please select a year between 2015 and {0}".format(datetime.now().year))
    elif selected_day < 1 or selected_day > 25:
        print("Invalid day! Please select a day between 1 and 25")
    elif (selected_day == datetime.now().day and selected_year == datetime.now().year) and datetime.now().month != 12:
        print("Invalid month! Please wait for december or select previous years".format(datetime.now().day))
    else:
        grab_input(dir_path, selected_year, selected_day, create_file)

    sys.exit()