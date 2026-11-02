import os
from aocd.models import Puzzle
from dotenv import load_dotenv, set_key
import sys

load_dotenv()

answer = ""

year = int(sys.argv[2]) if len(sys.argv) > 2 else int(os.getenv("YEAR"))
day = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.getenv("DAY"))

stage = sys.argv[3] if len(sys.argv) > 3 else "input"

if stage == "examp":
    file_name = f"examples/{year}/examp0_d{day}_y{year}.txt"
else:
    file_name = f"inputs/{year}/input_d{day}_y{year}.txt"

with open(file_name) as file:
    for file_line in file:
        line = file_line.strip()
        #x = x.split(" ")

print(answer)