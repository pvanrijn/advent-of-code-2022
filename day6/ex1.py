#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    transmission = f.read()

for i in range(len(transmission)):
    packet = set(transmission[i:i+4])
    if len(packet) == 4:
        print(i+4)
        break