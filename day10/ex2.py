#!/usr/bin/env python 3

f = open('input.txt', 'r')

cycle = 1
reg_val = 1
queue = ['']
line = ''
current_pixel = 0

while queue:

    instruction = next(f, '').rstrip()

    if instruction == 'noop':
        queue.append('')

    elif instruction:
        _, num = instruction.split()
        num = int(num)
        queue.append(num)
        queue.append('')

    sprite = [reg_val + n for n in [-1, 0, 1]]
    if current_pixel in sprite:
        line += '#'
    else:
        line += '.'
    current_pixel += 1

    add_val = queue.pop(0)
    if add_val:
        reg_val += add_val

    if cycle % 40 == 0:
        print(line)
        line = ''
        current_pixel = 0

    cycle += 1

f.close()