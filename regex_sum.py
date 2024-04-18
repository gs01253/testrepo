#!/usr/bin/env python3

import re
filename = 'regex_sum_real.txt'

def extract_numbers_and_sum(filename):
  with open(filename, 'r') as file:
    text = file.read()
    numbers = re.findall(r'\d+', text)
    numbers = [int(num) for num in numbers]
    total_sum = sum(numbers)
    return total_sum

total_sum = extract_numbers_and_sum(filename)

print(total_sum)
