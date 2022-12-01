#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    lines = [l.rstrip() for l in f.readlines()]

most_calories = []
curr_calories = 0

for l in lines:
    if not l:
        if len(most_calories) < 3:
            most_calories.append(curr_calories)
            most_calories.sort()
        elif any(curr_calories > most_cal for most_cal in most_calories):
            most_calories.pop(0)
            most_calories.append(curr_calories)
            most_calories.sort()
        curr_calories = 0
        continue
    curr_calories += int(l)

print(f'Most calories: {most_calories}')
print(f'Total most calories: {sum(most_calories)}')