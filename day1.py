# The Document indicates that you should start at the given coordinates (where you just landed) and face North.
# Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number
# of blocks, ending at a new intersection.
#
# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the
# destination. Given that you can only walk on the street grid of the city, how far is the shortest path to
# the destination?
import math
import numpy

def turn_right(d):
    return math.fmod(d + 90.0, 360.0)


def turn_left(d):
    return math.fmod(360.0 + d - 90.0, 360.0)


# instruction = 'R2, L3'
# instruction = 'R2, R2, R2'
# instruction = 'R5, L5, R5, R3'
instruction = 'R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5'
# instruction = 'R8, R4, R4, R8'

inList = instruction.split(', ')

print('Length: ' + str(len(inList)))
direction = 0.0 # Heading north
x = 0.0
y = 0.0

offset = 400
grid = numpy.zeros((800, 800))

for v in inList:
    if v[0] == 'R':
        direction = turn_right(direction)
    elif v[0] == 'L':
        direction = turn_left(direction)
    else:
        print('Unknown direction!')

    distance = int(v[1:])

    for ii in range(0,distance):
        x += round(math.cos(direction * math.pi / 180.0))
        y += round(math.sin(direction * math.pi / 180.0))

        if grid[int(x+offset), int(y+offset)] == 1:
            print('Found location! ' + str(x) + ", " + str(y) + ' distance: ' + str(abs(x)+abs(y)))
        grid[x + offset, y + offset] = 1


    print("@position " + str(x) + ", " + str(y))

print('Distance travelled: ' + str(abs(x)+abs(y)))



