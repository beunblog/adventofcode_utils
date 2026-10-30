import os
from aocd.models import Puzzle
from dotenv import load_dotenv, set_key
import sys

load_dotenv()

if __name__ == "__main__":

    year = int(sys.argv[2]) if len(sys.argv) > 2 else int(os.getenv("YEAR"))
    day = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.getenv("DAY"))

    puzzle = Puzzle(year, day)

    print(f"Data from day {day} of {year}: {puzzle.title} collected")

    for i, example in enumerate(puzzle.examples):
        with open(f"examples/examp{i}_d{day}_y{year}.txt", "w", encoding="utf-8") as f:
            f.write(example.input_data)
            if example.answer_a != None:
                set_key(dotenv_path=".env", key_to_set=f"ANSA_{i}_d{day}_y{year}", value_to_set=example.answer_a)
            if example.answer_b != None:
                set_key(dotenv_path=".env", key_to_set=f"ANS_B_{i}_d{day}_y{year}", value_to_set=example.answer_b)
    with open(f"inputs/input_d{day}_y{year}.txt", "w", encoding="utf-8") as f:
        f.write(puzzle.input_data)