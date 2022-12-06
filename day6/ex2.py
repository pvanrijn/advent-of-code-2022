#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    transmission = f.read()

for i in range(len(transmission)):
    packet = set(transmission[i:i+14])
    if len(packet) == 14:
        print(i+14)
        break