from datetime import datetime
from pathlib import Path

import requests

from core.config import AOC_COOKIE, INPUT_URL

class AdventOfCode:
    def __init__(
            self,
            root_path: Path,
        ) -> None:
        self._root_path = root_path

    def _copy_template(
            self,
            year: int,
            day: int,
            target_path: Path
        ) -> None:
        template_path = self._root_path / "templates" / "solution_template.py"

        content: str
        with template_path.open("r") as file:
            content = file.read()

        content.format(year=year, day=day)

        if not target_path.exists():
            target_path.touch()

        with target_path.open("w") as file:
            file.write(content)

    def grab_input(
            self,
            year: int,
            day: int,
            template: bool
        ) -> bool:
        # Validation
        if year < 2015 or year > datetime.now().year:
            print(f"Invalid year! Please select a year between 2015 and {datetime.now().year}")
            return False
        elif day < 1 or day > 25:
            print("Invalid day! Please select a day between 1 and 25")
            return False
        elif (
            day == datetime.now().day
            and year == datetime.now().year
            and datetime.now().month != 12):
            print("Invalid month! Please wait for december or select previous years")
            return False

        # Try to fetch the input
        print(f"Grabbing input for year {year} day {day}...")
        res = requests.get(
            INPUT_URL.format(year, day),
            cookies={"session":AOC_COOKIE}, # type: ignore
            headers={},
            timeout=10,
        )

        if res.status_code != 200:
            log_path = self._root_path / "error.log"

            with log_path.open("w") as file:
                file.write(f"{res.status_code}\n{res.text}")

            print(
                f"Error occured! Status code: {res.status_code}, text: {res.text}\nLog file created in {log_path}"
            )
            return False

        # Save the input
        path = self._root_path / "solutions" / str(year) / str(day)
        if not path.exists():
            path.mkdir(parents=True)

        input_file = path / "input.txt"
        if not input_file.exists():
            input_file.touch()

        with input_file.open("w") as file:
            file.write(res.text)
        print(f"Success! Input Saved to {input_file}")

        # Copy the template
        if template:
            solution_path = path / "main.py"
            self._copy_template(year, day, solution_path)
            print(f"Template succesfully copied to {solution_path}")

        return False

    def run_solution(
            self,
            day: int,
            year: int,
            profile: bool
        ) -> None:
        print("Sorry, running solutions is not implemented yet.")
