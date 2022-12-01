#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    lines = [l.rstrip() for l in f.readlines()]

most_calories = 0
curr_calories = 0

for l in lines:
    if not l:
        if curr_calories > most_calories:
            most_calories = curr_calories
        curr_calories = 0
        continue
    curr_calories += int(l)

print(f'Most calories: {most_calories}')