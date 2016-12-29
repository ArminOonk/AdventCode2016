from collections import namedtuple
import numpy
Point = namedtuple('Point', ['x', 'y'])

# fav_num = 10
# screen_width = 10
# screen_height = 10
# end_location = Point(7, 4)

fav_num = 1362
screen_width = 60
screen_height = 60
end_location = Point(31, 39)

def set_grid_value(point, val):
    grid[point.y, point.x] = val


def get_grid_value(point):
    return grid[point.y, point.x]


def is_wall(point):
    v = point.x * point.x + 3 * point.x + 2 * point.x * point.y + point.y + point.y * point.y + fav_num
    ones = sum([x == '1' for x in bin(v)[2:]])
    print('Number of 1: ' + str(ones))

    return ones % 2 == 1


grid = numpy.zeros((screen_height, screen_width))

start_location = Point(1, 1)


# Initialize grid
for x in range(0, screen_width):
    for y in range(0, screen_height):
        p = Point(x,y)
        if is_wall(p):
            set_grid_value(p, numpy.nan)

set_grid_value(start_location, 1)

wave = 1

# while get_grid_value(end_location) == 0:
while wave < 52:

    for x in range(0, screen_width):
        for y in range(0, screen_height):
            p = Point(x, y)
            v = get_grid_value(p)

            if get_grid_value(p) != wave:
                continue
            # We have found a point where the wave has hit

            if x+1 < screen_width:
                tmp = Point(x+1, y)
                if get_grid_value(tmp) == 0:
                    set_grid_value(tmp, v+1)
            if x-1 >= 0:
                tmp = Point(x-1, y)
                if get_grid_value(tmp) == 0:
                    set_grid_value(tmp, v+1)
            if y+1 < screen_height:
                tmp = Point(x, y+1)
                if get_grid_value(tmp) == 0:
                    set_grid_value(tmp, v+1)
            if y-1 >= 0:
                tmp = Point(x, y-1)
                if get_grid_value(tmp) == 0:
                    set_grid_value(tmp, v+1)
    wave += 1

print(numpy.array_str(grid, max_line_width=500))
print('Steps: ' + str(get_grid_value(end_location)-1))

tmp = numpy.nan_to_num(grid)

print('Unique locations: ' + str(numpy.count_nonzero(tmp)))

