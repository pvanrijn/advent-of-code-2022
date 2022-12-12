#!/usr/bin/env python3

from operator import sub


def distance(head, tail):
    return tuple(map(sub, tail, head))


def touching(head, tail):
    dist_x, dist_y = distance(head, tail)
    if abs(dist_x) <= 1 and abs(dist_y) <= 1:
        return True
    else:
        return False

def move_tail(head, tail, max_dist=1):
    dist_x, dist_y = distance(head, tail)
    head_x, head_y = head
    tail_x, tail_y = tail

    if dist_x < -max_dist:
        tail_x += max_dist
        tail_y = head_y

    elif dist_x > max_dist:
        tail_x -= max_dist
        tail_y = head_y

    if dist_y < -max_dist:
        tail_y += max_dist
        tail_x = head_x

    elif dist_y > max_dist:
        tail_y -= max_dist
        tail_x = head_x

    return (tail_x, tail_y)


with open('input.txt', 'r') as f:
    moves = [tuple(l.rstrip().split()) for l in f.readlines()]
    moves = [(drctn, int(num)) for drctn, num in moves]

# define whether to increase or decrease per direction
direction_steps   = {'U': 1, 'D': -1, 'L': -1, 'R': 1}

# get the tuple field that will be increased/decreased
update_x_or_y = {'U': 1,  'D': 1, 'L': 0,  'R': 0}

head = (0, 0)
tail = (0, 0)

tail_visited = set()
tail_visited.add(tail)  # set starting pos

for direction, num_steps in moves:

    # get increase/decrease for current direction
    range_step = direction_steps[direction]

    # get tuple field that increases/decreases each step
    alter_tupfield = update_x_or_y[direction]

    # get tuple field that doesn't change
    steady_tupfield = abs(alter_tupfield - 1)

    # set correct direction steps
    if range_step == 1:
        start = head[alter_tupfield] + 1
        end   = head[alter_tupfield] + num_steps + 1
    else:
        start = head[alter_tupfield] - 1
        end   = head[alter_tupfield] - num_steps - 1

    for step in range(start, end, range_step):

        # get new head position
        if alter_tupfield == 0:
            head = (step, head[steady_tupfield])
        else:
            head = (head[steady_tupfield], step)

        # move tail if head and tail are not adjacent
        if not touching(head, tail):
            tail = move_tail(head, tail)

        tail_visited.add(tail)

print(len(tail_visited))