#!/usr/bin/env python3

from itertools import islice
from string import ascii_lowercase, ascii_uppercase


values = {c: i for i, c in enumerate(ascii_lowercase+ascii_uppercase, start=1)}

with open('input.txt', 'r') as f:
    rucksacks = [l.rstrip() for l in f.readlines()]
    rucksacks = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

total_score = 0
for group in rucksacks:
    sack1, sack2, sack3 = map(set, map(list, group))
    item_in_common = next(iter(sack1 & sack2 & sack3))
    total_score += values[item_in_common]

print(f'Total score: {total_score}')