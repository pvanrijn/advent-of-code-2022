#!/usr/bin/env python3

import math
import re

monkeys = {}

with open('input.txt', 'r') as f:
    lines = [l.rstrip() for l in f.readlines() if l.rstrip()]

    for i, line in enumerate(lines):

        if not line.startswith('Monkey'):
            continue

        monkeynum = int(line.split()[-1].rstrip(':'))
        monkeys[monkeynum] = {'items': [], 'operation': None, 'test': None}

        starting_items = list(map(int, re.findall('\d+', lines[i+1])))
        monkeys[monkeynum]['items'] = starting_items

        monkeys[monkeynum]['operation'] = lines[i+2].split('= ')[-1].replace('old', 'item')

        monkeys[monkeynum]['division'] = int(re.search('\d+', lines[i+3]).group())
        monkeys[monkeynum]['divtrue'] = int(lines[i+4][-1])
        monkeys[monkeynum]['divfalse'] = int(lines[i+5][-1])


inspect_count = {}

print(monkeys)

for _ in range(20):
    for monkey, monkeydict in monkeys.items():
        while monkeydict['items']:
            item = monkeydict['items'].pop(0)
            item = math.floor((eval(monkeydict['operation'])) / 3)
            pass_to_monkey = monkeys[monkey]['divtrue'] if item % monkeydict['division'] == 0 else monkeydict['divfalse']
            monkeys[pass_to_monkey]['items'].append(item)

            inspect_count[monkey] = inspect_count.get(monkey, 0) + 1

print(inspect_count)

top2 = sorted(inspect_count.values(), reverse=True)[:2]

print(top2[0] * top2[1])