#!/usr/bin/env python3

def is_touching(head, tail):
    pass

with open('input.txt', 'r') as f:
    moves = [tuple(l.rstrip().split()) for l in f.readlines()]
    moves = [(drctn, int(num)) for drctn, num in moves]

range_steps   = {'U': -1, 'D': 1, 'L': -1, 'R': 1}
update_x_or_y = {'U': 1,  'D': 1, 'L': 0,  'R': 0}

head = (0, 0)
tail = (0, 0)

positions_visited = set()
positions_visited.add(head)

for direction, num_steps in moves:

    range_step = range_steps[direction]
    x_or_y = update_x_or_y[direction]

    for step in range(head[x_or_y], head[x_or_y]+num_steps, range_step):
        head =
        positions_visited.add(head)