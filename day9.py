
length = 0
# line = 'A(1x5)BC'
# line = '(3x3)XYZ'
# line = 'A(2x2)BCD(2x2)EFG'
# line = '(6x1)(1x3)A'
# line = 'X(8x2)(3x3)ABCY'

with open('inputDay9.txt', 'r') as f:
    lines = f.readlines()

print("number of lines: " + str(len(lines)))
line = lines[0].strip()

# line = '(3x3)XYZ'
# line = 'X(8x2)(3x3)ABCY'
# line = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
# line = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

def decompress_length(l):
    print('Decomp: ' + l)
    tmp_length = 0

    try:
        start_marker = l.index('(')
        end_marker = l.index(')')
    except:
        print('No start/end marker found')
        return len(l), ''

    v = l[start_marker + 1:end_marker].split('x')
    if len(v) == 2:
        repeat_length = int(v[0])
        repeat_count = int(v[1])

        inner_line = l[end_marker+1:end_marker+repeat_length+1]
        # print('inner_line: ' + inner_line)
        while len(inner_line) > 0:
            il, inner_line = decompress_length(inner_line)
            tmp_length += repeat_count * il

    tmp_length += start_marker
    return tmp_length, l[end_marker+repeat_length+1:]

while len(line) > 0:
    t_length, line = decompress_length(line)
    length += t_length

    # try:
    #     start_marker = line.index('(')
    #     end_marker = line.index(')')
    # except:
    #     length += len(line)
    #     print('Last part of the string: ' + line)
    #     print('Final length: ' + str(length))
    #     quit()
    #
    # # print('Marker: ' + line[start_marker + 1:end_marker])
    # v = line[start_marker + 1:end_marker].split('x')
    # if len(v) == 2:
    #     repeat_length = int(v[0])
    #     repeat_count = int(v[1])
    #
    #     # print('start marker: ' + str(start_marker))
    #     # print('end marker: ' + str(end_marker))
    #     length += start_marker + repeat_length*repeat_count
    #
    #     line = line[end_marker+repeat_length+1:]
    #     # print('remaining line: ' + line)
    # else:
    #     print('Incorrect length in the marker')
    #     print('Stopping at position: ' + line[:10])
    #     print('Incorrect length: ' + str(length))

print('Length: ' + str(length))