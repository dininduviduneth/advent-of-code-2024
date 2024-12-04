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

def extract_valid_mul_expressions(text):
    # Define the regex patterns
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Find all occurrences of "do()" and "don't()"
    do_positions = [m.start() for m in re.finditer(do_pattern, text)]
    dont_positions = [m.start() for m in re.finditer(dont_pattern, text)]

    # Initialize the result list and the state
    result = []
    can_capture = True  # Initially, we can capture mul() expressions

    # Iterate over all mul() matches
    for match in re.finditer(mul_pattern, text):
        mul_start = match.start()

        # Check if the current mul() is after a "don't()" without a subsequent "do()"
        if any(dont_pos < mul_start for dont_pos in dont_positions):
            # Find the last "don't()" before this mul()
            last_dont_pos = max(dont_pos for dont_pos in dont_positions if dont_pos < mul_start)
            # Check if there's a "do()" after the last "don't()" and before this mul()
            if not any(do_pos > last_dont_pos and do_pos < mul_start for do_pos in do_positions):
                can_capture = False
            else:
                can_capture = True
        else:
            can_capture = True

        # If we can capture, add the mul() to the result
        if can_capture:
            result.append(match.group())

    return result

# Example usage
matches = extract_valid_mul_expressions(data)

multiples = []

for match in matches:
    pattern = r"\d{1,3}"
    numbers = re.findall(pattern, match)

    multiples.append(int(numbers[0]) * int(numbers[1]))

print(f"Result: {sum(multiples)}")