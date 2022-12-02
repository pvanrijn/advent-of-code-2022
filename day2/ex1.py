#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    plays = [l.rstrip().split() for l in f.readlines()]

scores = {'A': {'X': 4, 'Y': 8, 'Z': 3},
          'B': {'X': 1, 'Y': 5, 'Z': 9},
          'C': {'X': 7, 'Y': 2, 'Z': 6}}

print('Finale score:', sum(scores[a][b] for a, b in plays))