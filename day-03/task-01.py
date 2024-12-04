import sys
import os
import re

# Adding the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.fetch_data import extraction

# Extracting data and saving to data.txt
extraction(2024, 3)

# Reading data from data.txt
with open('data.txt', 'r') as file:
    data = file.read()

# Fetch regex matches
pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, data)

multiples = []

for match in matches:
    pattern = r"\d{1,3}"
    numbers = re.findall(pattern, match)

    multiples.append(int(numbers[0]) * int(numbers[1]))

print(f"Result: {sum(multiples)}")