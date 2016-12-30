from collections import namedtuple
import hashlib


def get_hash(txt):
    m = hashlib.md5()
    m.update(bytes(txt, 'utf-8'))
    return m.hexdigest()


def directions(path, pos):
    h = get_hash(path)[0:4]
    d = []

    for c in h:
        if c.isnumeric() or c == 'a':
            d.append(False)
        else:
            d.append(True)
    if pos.y == 0:
        d[0] = False  # Wall Up direction
    if pos.y == 3:
        d[1] = False  # Wall Down direction
    if pos.x == 0:
        d[2] = False  # Wall Left direction
    if pos.x == 3:
        d[3] = False  # Wall right direction

    return d


def is_end(pos):
    return pos.x == 3 and pos.y == 3


Point = namedtuple('Point', ['x', 'y'])
width = 4
height = 4

# passcode = 'hijkl'
# passcode = 'ihgpwlah'
# passcode = 'kglvqrro'
# passcode = 'ulqzkmiv'
passcode = 'mmsxrhfx'

paths = [{'path': passcode, 'pos': Point(0, 0)}]

loop_cnt = 0
length_longest_path = 0
while True:
    new_paths = []
    for p in paths:

        d = directions(p['path'], p['pos'])

        if d[0]:
            new_pos = Point(p['pos'].x, p['pos'].y-1)
            cur_path = p['path']+'U'
            if is_end(new_pos):
                print('End reached: ' + cur_path[len(passcode):])
                if len(cur_path[len(passcode):]) > length_longest_path:
                    length_longest_path = len(cur_path[len(passcode):])
            else:
                new_paths.append({'path': cur_path, 'pos': new_pos})

        if d[1]:
            new_pos = Point(p['pos'].x, p['pos'].y+1)
            cur_path = p['path'] + 'D'
            if is_end(new_pos):
                print('End reached: ' + cur_path[len(passcode):])
                if len(cur_path[len(passcode):]) > length_longest_path:
                    length_longest_path = len(cur_path[len(passcode):])
            else:
                new_paths.append({'path': cur_path, 'pos': new_pos})

        if d[2]:
            new_pos = Point(p['pos'].x-1, p['pos'].y)
            cur_path = p['path'] + 'L'
            if is_end(new_pos):
                print('End reached: ' + cur_path[len(passcode):])
                if len(cur_path[len(passcode):]) > length_longest_path:
                    length_longest_path = len(cur_path[len(passcode):])
            else:
                new_paths.append({'path': cur_path, 'pos': new_pos})

        if d[3]:
            new_pos = Point(p['pos'].x+1, p['pos'].y)
            cur_path = p['path'] + 'R'
            if is_end(new_pos):
                print('End reached: ' + cur_path[len(passcode):])
                if len(cur_path[len(passcode):]) > length_longest_path:
                    length_longest_path = len(cur_path[len(passcode):])
            else:
                new_paths.append({'path': cur_path, 'pos': new_pos})

    paths = new_paths
    print('Number of new paths: ' + str(len(paths)))
    if len(new_paths) == 0:
        break

print('Longest path length: ' + str(length_longest_path))