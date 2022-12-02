#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    plays = [l.rstrip().split() for l in f.readlines()]

scores = {'A': {'X': 4, 'Y': 8, 'Z': 3},
          'B': {'X': 1, 'Y': 5, 'Z': 9},
          'C': {'X': 7, 'Y': 2, 'Z': 6}}

lose = {'X': {'A': 'Z', 'B': 'X', 'C': 'Y'},
        'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'},
        'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'}}

total_score = 0

for play, move in plays:
    total_score += scores[play][lose[move][play]]

print('Finale score:', total_score)