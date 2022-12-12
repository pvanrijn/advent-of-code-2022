#!/usr/bin/env python3

from operator import sub
from copy import deepcopy


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

    # right
    if dist_x < -max_dist:
        tail_x += max_dist
        if tail_y < head_y:
            tail_y += max_dist
        elif tail_y > head_y:
            tail_y -= max_dist

    # left
    elif dist_x > max_dist:
        tail_x -= max_dist
        if tail_y < head_y:
            tail_y += max_dist
        elif tail_y > head_y:
            tail_y -= max_dist

    # up
    elif dist_y < -max_dist:
        tail_y += max_dist
        if tail_x < head_x:
            tail_x += max_dist
        elif tail_x > head_x:
            tail_x -= max_dist

    # down
    elif dist_y > max_dist:
        tail_y -= max_dist
        if tail_x < head_x:
            tail_x += max_dist
        elif tail_x > head_x:
            tail_x -= max_dist

    # # shift right
    # if dist_x < 0 and dist_x < -max_dist:
    #     tail_x += max_dist
    #     tail_y = head_y

    # # shift left
    # elif dist_x > 0 and dist_x > max_dist:
    #     tail_x -= max_dist
    #     tail_y = head_y

    # # shift up
    # elif dist_y < 0 and dist_y < -max_dist:
    #     tail_y += max_dist
    #     tail_x += head_x

    # # shift down
    # elif dist_y > 0 and dist_y > max_dist:
    #     tail_y -= max_dist
    #     tail_x = head_x

    return (tail_x, tail_y)


with open('input.txt', 'r') as f:
    moves = [tuple(l.rstrip().split()) for l in f.readlines()]
    moves = [(drctn, int(num)) for drctn, num in moves]

# define whether to increase or decrease per direction
direction_steps   = {'U': 1, 'D': -1, 'L': -1, 'R': 1}

# get the tuple field that will be increased/decreased
update_x_or_y = {'U': 1,  'D': 1, 'L': 0,  'R': 0}

head = (0, 0)
tail_train = [(0, 0) for _ in range(9)]

tail_visited = set()

for direction, num_steps in moves:

    print(f'# Direction: {direction}, Steps: {num_steps}')

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

        tails = deepcopy(tail_train)
        cur_head = head

        for i, cur_tail in enumerate(tails):

            if not touching(cur_head, cur_tail):
                cur_tail = move_tail(cur_head, cur_tail)
                tail_train[i] = cur_tail

            if i + 1 == len(tails):
                tail_visited.add(cur_tail)

            cur_head = cur_tail

print(len(tail_visited))