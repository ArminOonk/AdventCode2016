import numpy
from datetime import datetime
from itertools import *


def find_distances(start, loc, g):
    distances = []

    height, width = g.shape

    for l in loc:
        g[l['y'], l['x']] = -(int(l['loc']) + 1)

    wave = 1
    g[start['y'], start['x']] = wave

    while True:
        has_changed = False
        for x in range(0, width):
            for y in range(0, height):
                if g[y, x] == wave:
                    # We are at a boundary of the wave
                    if y+1 < height:
                        if g[y+1, x] == 0:
                            g[y + 1, x] = wave + 1
                            has_changed = True
                        if g[y+1, x] < 0:
                            # Found a location
                            distances.append({'from': int(start['loc']), 'to': -(g[y + 1, x] + 1), 'dist': wave})
                            g[y + 1, x] = wave + 1
                            has_changed = True

                    if y - 1 >= 0:
                        if g[y - 1, x] == 0:
                            g[y - 1, x] = wave + 1
                            has_changed = True

                        if g[y - 1, x] < 0:
                            # Found a location
                            distances.append({'from': int(start['loc']), 'to': -(g[y - 1, x] + 1), 'dist': wave})
                            g[y - 1, x] = wave + 1
                            has_changed = True

                    if x + 1 < width:
                        if g[y, x+1] == 0:
                            g[y, x + 1] = wave + 1
                            has_changed = True

                        if g[y, x + 1] < 0:
                            distances.append({'from': int(start['loc']), 'to': -(g[y, x + 1] + 1), 'dist': wave})
                            g[y, x + 1] = wave + 1
                            has_changed = True

                    if x - 1 >= 0:
                        if g[y, x-1] == 0:
                            g[y, x - 1] = wave + 1
                            has_changed = True

                        if g[y, x - 1] < 0:
                            distances.append({'from': int(start['loc']), 'to': -(g[y, x - 1] + 1), 'dist': wave})
                            g[y, x - 1] = wave + 1
                            has_changed = True

        wave += 1
        if not has_changed:
            break

    return distances


def make_key(key):
    key_list = list(key)
    key_list.sort()
    return ''.join(key_list)


with open('inputDay25.txt', 'r') as f:
    data = f.readlines()

points = []
for d in data:
    for c in d:
        if c != '#' and c != '.' and c != '\n' and c != '0':
            points.append(c)

points.sort()
last_point = int(points[-1])
print(str(points) + ' last one: ' + str(last_point))

width = len(data[0])
height = len(data)

grid = numpy.zeros((height, width))
locations = []

for y in range(0, len(data)):
    if not data[y]:
        continue

    for x in range(0, len(data[0])):
        c = data[y][x]

        if c == '#':
            grid[y, x] = numpy.nan

        if c.isnumeric():
            locations.append({'loc': c, 'x': x, 'y': y})

print(locations)

start = datetime.now()
distances_found = []

for l in locations:
    distances_found += find_distances(start=l, loc=locations, g=numpy.copy(grid))

print('Search took: ' + str((datetime.now() - start).total_seconds()) + ' sec')

distances_sparse = dict()
for d in distances_found:
    key = make_key(str(int(d['from'])) + str(int(d['to'])))
    distances_sparse[key] = d['dist']

for key, value in distances_sparse.items():
    print(key + ' ' + str(value))

possible_routes = permutations(''.join(points))
shortest_distance = 999999999999999999
shortest_route = ''
for pr in possible_routes:
    route = '0' + ''.join(pr)

    distance = 0
    for x in range(2, len(route)+1):
        key = make_key(route[(x-2):x])
        distance += distances_sparse[key]

    if distance < shortest_distance:
        shortest_distance = distance
        shortest_route = route

    print('route: ' + route + ' distance: ' + str(distance))

print('Shortest routes: ' + shortest_route + ' distance ' + str(shortest_distance))
