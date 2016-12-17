import numpy

screen_width = 50
screen_height = 6
grid = numpy.zeros((screen_height, screen_width))


def rect(width, height):
    for x in range(0, width):
        for y in range(0, height):
            grid[y,x] = 1


def rotate_row(row, pixels):
    for i in range(0, pixels):
        pixel_to_left = grid[row, screen_width - 1]
        for y in range(screen_width-1, 0, -1):
            grid[row, y] = grid[row, y-1]
        grid[row, 0] = pixel_to_left


def rotate_colom(colom, pixels):
    for i in range(0, pixels):
        pixel_to_top = grid[screen_height - 1, colom]
        for x in range(screen_height-1, 0, -1):
            grid[x, colom] = grid[x-1, colom]
        grid[0, colom] = pixel_to_top

with open('inputDay8.txt') as f:
    for line in f.readlines():
        if line.startswith('rect'):
            v = line[4:].split('x')
            if len(v) == 2:
                rect(width=int(v[0]), height=int(v[1]))
            else:
                print('Reading rect but not enough parts')
        elif line.startswith('rotate column'):
            v = line[16:].split(' by ')
            if len(v) == 2:
                rotate_colom(colom=int(v[0]), pixels=int(v[1]))
            else:
                print('Reading rotate column but not enough parts')
        elif line.startswith('rotate row'):
            v = line[13:].split(' by ')
            if len(v) == 2:
                rotate_row(row=int(v[0]), pixels=int(v[1]))
            else:
                print('Reading rotate column but not enough parts')
        else:
            print('Unknown command')
        print('line: ' + line)


# rect(width=3, height=2)
# rotate_colom(colom=1, pixels=1)
# rotate_row(row=0, pixels=4)
# rotate_colom(colom=1, pixels=1)

print(numpy.array_str(grid, max_line_width=500))
values, counts = numpy.unique(grid, return_counts=True)
print('Values: ' + str(values))
print('Counts: ' + str(counts))


for x in range(0, screen_width-1, 5):
    print(grid[:, x:x+5])