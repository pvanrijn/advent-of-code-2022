#!/usr/bin/env python3

def nested_get(d, keys):
    for key in keys:
        d = d[key]
    return d

def nested_set(d, keys, values):
    if len(keys) > 1:
        for key in keys[:-1]:
            d = d.setdefault(key, {})

    key = keys[-1]

    val_type, val = values
    if val_type == 'dir':
        d[key][val] = d[key].get(val, {})
    else:
        val_type, val = val, int(val_type)
        d[key][val_type] = val

def traverse(d, levels=[], sums={}):
    for k, v in d.items():
        if isinstance(v, dict):
            levels.append(k)
            sums = traverse(v, sums=sums, levels=levels)
        else:
            traverse_levels = [levels[0:i] for i in range(1, len(levels)+1)]
            traverse_levels = list(map(lambda x: '_'.join(x), traverse_levels))
            for level in traverse_levels:
                sums[level] = sums.get(level, 0) + v
    if levels:
        levels.pop()
    return sums


with open('input.txt', 'r') as f:
    lines = [l.rstrip() for l in f.readlines()]

dirs = {'/': {}}
cur_dir_tree = []

for line in lines:
    args = line.split()
    if args[0] == '$':
        if args[1] == 'cd':
            if args[2] == '..':
                cur_dir_tree.pop()
            else:
                cur_dir_tree.append(args[2])
    else:
        nested_set(dirs, cur_dir_tree, args)


dir_sizes = traverse(dirs)
# print(dir_sizes)
total = sum(v for v in dir_sizes.values() if v <= 100_000)
print(f'Total file size: {total}')