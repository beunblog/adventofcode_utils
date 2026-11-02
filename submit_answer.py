import os
from aocd.models import Puzzle
from dotenv import load_dotenv, set_key
import sys

load_dotenv()

year = int(sys.argv[2]) if len(sys.argv) > 2 else int(os.getenv("YEAR"))
day = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.getenv("DAY"))

answer = sys.argv[3]
part = sys.argv[4] if len(sys.argv) > 4 else "a"

puzzle = Puzzle(year, day)

if answer is not None and part == "a":
    puzzle.answer_a = answer
elif answer is not None and part == "b":
    puzzle.answer_b = answer
else:
    print("Invalid parameters, please fill in the date, the part and the answer.")




