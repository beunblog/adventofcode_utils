import os
from aocd.models import Puzzle
from dotenv import load_dotenv, set_key
import sys
from pathlib import Path
import shutil
from datetime import datetime


if not Path(f".env").exists():
    f = open(".env", "x")

    set_key(dotenv_path=".env", key_to_set="YEAR", value_to_set=str(datetime.now().year))
    set_key(dotenv_path=".env", key_to_set="DAY", value_to_set=str(datetime.now().day))
    set_key(dotenv_path=".env", key_to_set="AOC_SESSION", value_to_set="")

    print("Script terminated, please fill in your AOC session token in de created .env file. Then rerun the script.")

    sys.exit()

load_dotenv()

year = int(sys.argv[2]) if len(sys.argv) > 2 else int(os.getenv("YEAR"))
day = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.getenv("DAY"))

puzzle = Puzzle(year, day)

puzzle.view()

path_file = f"{year}"

if not os.path.exists(path_file):
    os.makedirs(path_file)

desta = Path(str(year)) / f"file_a_d{day}_y{year}.py"

if not desta.exists():
    desta.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy("template.py", desta)
else:
    print(f"{desta} already exists, skipping")

destb = Path(str(year)) / f"file_b_d{day}_y{year}.py"

if not destb.exists():
    destb.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy("template.py", destb)
else:
    print(f"{destb} already exists, skipping")


for i, example in enumerate(puzzle.examples):
    path_example = f"{year}/examples"
    file_example = f"examp{i}_d{day}_y{year}.txt"

    if not os.path.exists(path_example):
        os.makedirs(path_example)

    with open(os.path.join(path_example, file_example), "w", encoding="utf-8") as f:
        f.write(example.input_data)
        if example.answer_a is not None:
            set_key(dotenv_path=".env", key_to_set=f"ANSA_{i}_d{day}_y{year}", value_to_set=example.answer_a)
        if example.answer_b is not None:
            set_key(dotenv_path=".env", key_to_set=f"ANSB_{i}_d{day}_y{year}", value_to_set=example.answer_b)

path_input = f"{year}/inputs"
file_input = f"input_d{day}_y{year}.txt"

if not os.path.exists(path_input):
    os.makedirs(path_input)

with open(os.path.join(path_input, file_input), "w", encoding="utf-8") as f:
    f.write(puzzle.input_data)



print(f"Data from day {day} of {year}: {puzzle.title} collected")