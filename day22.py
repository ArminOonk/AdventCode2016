def is_viable_pair(a, b):
    if a == b:
        return False

    if a['used'] == 0:
        return False

    if a['used'] > b['avail']:
        return False

    return True



with open('inputDay22.txt', 'r') as f:
    data = f.readlines()

disks = []

for d in data:
    if d.startswith('/dev'):
        vals = [x for x in d.strip().split(' ') if x]
        pos_str = vals[0][15:]
        pos_vals = pos_str.split('-')

        x = int(pos_vals[0][1:])
        y = int(pos_vals[1][1:])

        if vals[1][len(vals[1])-1] != 'T':
            print('Size Not Tera!')

        size = int(vals[1][:len(vals[1])-1])

        if vals[2][len(vals[2])-1] != 'T':
            print('Used Not Tera!')

        used = int(vals[2][:len(vals[2]) - 1])

        if vals[3][len(vals[3])-1] != 'T':
            print('Avail Not Tera!')

        avail = int(vals[3][:len(vals[3]) - 1])

        # print(vals)
        # print('position: ' + str(x) + ' ' + str(y) + ' size: ' + str(size) + ' used: ' + str(used) + ' avail: ' + str(avail))

        disks.append({'x': x, 'y': y, 'size': size, 'used': used, 'avail': avail})

print('Loaded ' + str(len(disks)) + ' disks')
viable_pairs = []
cnt = 0
for a in disks:
    for b in disks:
        if is_viable_pair(a, b):
            viable_pairs.append({'a': a, 'b': b})
    cnt += 1
    if cnt%50 == 0:
        print('Cnt: ' + str(cnt))

print('Number of viable pairs: ' + str(len(viable_pairs)))
