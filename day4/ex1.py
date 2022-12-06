#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    assignments = [tuple(l.rstrip().split(',')) for l in f.readlines()]

overlaps = 0
for elf1, elf2 in assignments:
    elf1, elf2 = tuple(map(int, elf1.split('-'))), tuple(map(int, elf2.split('-')))
    elf1, elf2 = set(range(elf1[0], elf1[1]+1)), set(range(elf2[0], elf2[1]+1))
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        overlaps += 1

print('Total overlaps:', overlaps)