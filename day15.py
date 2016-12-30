
with open('inputDay15.txt', 'r') as f:
    data = f.readlines()

discs = []
for d in data:
    vals = d[12:].split('position')

    size = int(vals[0])
    offset = int(vals[2][1])

    discs.append({'size': size, 'offset': offset})
    print('Size: ' + str(size) + ' offset: ' + str(offset))

t = 0

while True:
    position = []
    for x in range(0, len(discs)):
        disc = discs[x]
        p = (disc['offset'] + t + x + 1) % disc['size']

        position.append(p)

    print('Position: ' + str(position))

    is_good_option = True
    for p in position:
        if p != 0:
            is_good_option = False
            break

    if is_good_option:
        print('First good option: ' + str(t))
        quit()

    t += 1

