#!/usr/bin/env python3

def trees(tx, ty, edge_x, edge_y):
    up    = [(tx, y) for y in range(ty-1, -1, -1)]
    down  = [(tx, y) for y in range(ty+1, edge_y)]
    left  = [(x, ty) for x in range(tx-1, -1, -1)]
    right = [(x, ty) for x in range(tx+1, edge_x)]
    return up, down, left, right


with open('input.txt', 'r') as f:
    lines = [l.rstrip() for l in f.readlines()]
    mat = [[int(n) for n in l] for l in lines]

edge_x = len(mat[0])
edge_y = len(mat)

visible_trees = 0

for cur_y, row in enumerate(mat):

    for cur_x, val in enumerate(row):
        if (cur_y == 0 or cur_y == edge_y-1) or (cur_x == 0 or cur_x == edge_x-1):
            visible_trees += 1
            continue

        up, down, left, right = trees(cur_x, cur_y, edge_x, edge_y)

        up    = all([mat[y][x] < val for x, y in up])
        down  = all([mat[y][x] < val for x, y in down])
        left  = all([mat[y][x] < val for x, y in left])
        right = all([mat[y][x] < val for x, y in right])

        lines_of_sight = [up, down, left, right]

        if any(los for los in lines_of_sight):
            visible_trees += 1

print(visible_trees)