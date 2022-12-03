#!/usr/bin/env python3

from string import ascii_lowercase, ascii_uppercase


values = {c: i for i, c in enumerate(ascii_lowercase+ascii_uppercase, start=1)}

with open('input.txt', 'r') as f:
    rucksacks = [l.rstrip() for l in f.readlines()]

total_score = 0
for rucksack in rucksacks:
    half = len(rucksack) // 2
    first_half, second_half = set(list(rucksack[:half])), set(list(rucksack[half:]))
    item_in_common = next(iter(first_half & second_half))
    total_score += values[item_in_common]

print(f'Total score: {total_score}')