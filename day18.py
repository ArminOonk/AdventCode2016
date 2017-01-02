
result = []
# result.append('.^^.^.^^^^')
# extra_rows = 9
result.append('.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^')
extra_rows = 399999

for i in range(0, extra_rows):
    next_line = ''
    for x in range(0, len(result[i])):

        if x == 0:
            left_is_trap = False
        else:
            left_is_trap = result[i][x - 1] == '^'

        center_is_trap = result[i][x] == '^'

        if x == len(result[i])-1:
            right_is_trap = False
        else:
            right_is_trap = result[i][x + 1] == '^'

        if left_is_trap and center_is_trap and not right_is_trap:
            next_line += '^'
        elif not left_is_trap and center_is_trap and right_is_trap:
            next_line += '^'
        elif left_is_trap and not center_is_trap and not right_is_trap:
            next_line += '^'
        elif not left_is_trap and not center_is_trap and right_is_trap:
            next_line += '^'
        else:
            next_line += '.'
    result.append(next_line)

print('Result')
safe_tiles = 0
for res in result:
    for r in res:
        if r == '.':
            safe_tiles += 1
    # print(res)

print('Safe tiles: ' + str(safe_tiles))



