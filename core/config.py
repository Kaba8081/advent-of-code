import os
from dotenv import load_dotenv

load_dotenv()

AOC_COOKIE = os.getenv("AOC_COOKIE")
INPUT_URL = "https://adventofcode.com/{0}/day/{1}/input"
