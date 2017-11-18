import numpy
from datetime import datetime


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

    # print(grid)
    # for d in distances:
    #     print(d)

    return distances


with open('testInputDay24.txt', 'r') as f:
    data = f.readlines()

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

start = datetime.now()
distances_found = []
for l in locations:
    distances_found += find_distances(start=l, loc=locations, g=numpy.copy(grid))

print('Search took: ' + str((datetime.now() - start).total_seconds()) + ' sec')

for d in distances_found:
    print(d)


