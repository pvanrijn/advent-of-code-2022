#!/usr/bin/env python3

import re

# [T]             [P]     [J]
# [F]     [S]     [T]     [R]     [B]
# [V]     [M] [H] [S]     [F]     [R]
# [Z]     [P] [Q] [B]     [S] [W] [P]
# [C]     [Q] [R] [D] [Z] [N] [H] [Q]
# [W] [B] [T] [F] [L] [T] [M] [F] [T]
# [S] [R] [Z] [V] [G] [R] [Q] [N] [Z]
# [Q] [Q] [B] [D] [J] [W] [H] [R] [J]
#  1   2   3   4   5   6   7   8   9

stacks = {1: ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'],
          2: ['Q', 'R', 'B'],
          3: ['B', 'Z', 'T', 'Q', 'P', 'M', 'S'],
          4: ['D', 'V', 'F', 'R', 'Q', 'H'],
          5: ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'],
          6: ['W', 'R', 'T', 'Z'],
          7: ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'],
          8: ['R', 'N', 'F', 'H', 'W'],
          9: ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']}

with open('input.txt', 'r') as f:
    moves = [tuple(map(int, [m.group() for m in re.finditer(r'\d+', l)])) for l in f.readlines()]

for num_crates, move_from, move_to in moves:
    stacks[move_to] += stacks[move_from][-num_crates:]
    stacks[move_from] = stacks[move_from][:-num_crates]

top_crates = ''.join(crates[-1] for stack, crates in stacks.items())
print(top_crates)