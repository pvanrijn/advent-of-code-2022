#!/usr/bin/env python3

def trees(tx, ty, edge_x, edge_y):
    up    = [(tx, y) for y in range(ty-1, -1, -1)]
    down  = [(tx, y) for y in range(ty+1, edge_y)]
    left  = [(x, ty) for x in range(tx-1, -1, -1)]
    right = [(x, ty) for x in range(tx+1, edge_x)]
    return up, down, left, right

def trees_in_los(trs, val):
    tree_count = 0
    for tree in trs:
        tree_count += 1
        if tree >= val:
            break
    return tree_count

with open('input.txt', 'r') as f:
    lines = [l.rstrip() for l in f.readlines()]
    mat = [[int(n) for n in l] for l in lines]

edge_x = len(mat[0])
edge_y = len(mat)

best_sight = 0

for cur_y, row in enumerate(mat):

    for cur_x, val in enumerate(row):

        up, down, left, right = trees(cur_x, cur_y, edge_x, edge_y)

        up    = trees_in_los([mat[y][x] for x, y in up], val)
        down  = trees_in_los([mat[y][x] for x, y in down], val)
        left  = trees_in_los([mat[y][x] for x, y in left], val)
        right = trees_in_los([mat[y][x] for x, y in right], val)

        sight = up * down * left * right

        if sight > best_sight:
            best_sight = sight

print(best_sight)