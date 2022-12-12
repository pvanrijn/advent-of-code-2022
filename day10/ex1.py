#!/usr/bin/env python 3

f = open('input.txt', 'r')

cycle = 1
reg_val = 1
sum_at_cycle = 20
queue = ['']
total_sum = 0

while queue:

    if cycle == sum_at_cycle:
        print(f'# {cycle} * {reg_val} = {cycle*reg_val}')
        total_sum += cycle * reg_val
        sum_at_cycle += 40

    instruction = next(f, '').rstrip()

    if instruction == 'noop':
        queue.append('')

    elif instruction:
        _, num = instruction.split()
        num = int(num)
        queue.append(num)
        queue.append('')

    add_val = queue.pop(0)
    if add_val:
        reg_val += add_val

    cycle += 1

print(total_sum)

f.close()