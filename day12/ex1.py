#!/usr/bin/env python3

import collections
from pprint import pprint


def fetch_neighbors(x, y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

# def bfs(heightmap, start, end):
#     length = 0
#     path = []
#     queue = collections.deque([(start, path, length)])
#     seen = set([start])

#     while queue:
#         node, path, length = queue.popleft()
#         if node == end:
#             return path, length

#         neighbors = fetch_neighbors(*node)
#         for neighbor in neighbors:
#             diff = heightmap[node] - heightmap.get(neighbor, float('inf'))
#             if diff >= -1 and neighbor not in seen:
#                 length += 1
#                 path.append(neighbor)
#                 queue.append((neighbor, path[:], length))
#                 seen.add(node)
#                 # check for common neighbors, don't increment length when common

#     return path, length

def bfs(heightmap, start, end):
    path = [start]
    queue = collections.deque([path])
    seen = set()

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path, length

        neighbors = fetch_neighbors(*node)
        for neighbor in neighbors:
            diff = heightmap[node] - heightmap.get(neighbor, float('inf'))
            if diff >= -1 and neighbor not in seen:
                length += 1
                path.append(neighbor)
                queue.append((neighbor, path[:], length))
                seen.add(node)
                # check for common neighbors, don't increment length when common

    return path, length


def print_path(mat, path):
    for y, row in enumerate(mat):
        print(''.join(['@' if (x, y) in path else c for x, c in enumerate(row)]))


with open('input.txt', 'r') as f:
    mat = [list(l.rstrip()) for l in f.readlines()]

start = (0, 0)
end = (0, 0)
heightmap = {}

for y, row in enumerate(mat):
    for x, col in enumerate(row):
        if col == 'S':
            start = (x, y)
            col = 'a'
        if col == 'E':
            end = (x, y)
            col = 'z'
        heightmap[(x, y)] = ord(col)

print(f'Start: {start}')
print(f'End: {end}')

best_path, length = bfs(heightmap, start, end)

print_path(mat, best_path)
print(length)