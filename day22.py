from datetime import datetime

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
max_x = 0
max_y = 0

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

        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

        disks.append({'x': x, 'y': y, 'size': size, 'used': used, 'avail': avail})

print('Loaded ' + str(len(disks)) + ' disks')
print('Grid size: ' + str(max_x) + ' ' + str(max_y))
for a in disks:
    if a['x'] == max_x and a['y'] == 0:
        target_disk = a
        break
print('Target disk: ' + str(target_disk))

for a in disks:
    if a['size'] < target_disk['used']:
        print('Not enough space available: ' + str(a['x']) + ' ' + str(a['y']))

    if a['used'] == 0:
        print('Empty node: ' + str(a['x']) + ' ' + str(a['y']))

    if a['y'] == 0:
        print('x: ' + str(a['x']) + ' used: ' + str(a['used']) + ' avail: ' + str(a['avail']) + ' size: ' + str(a['size']))


viable_pairs = []
cnt = 0
start = datetime.now()
for a in disks:
    for b in disks:
        if is_viable_pair(a, b):
            viable_pairs.append({'a': a, 'b': b})
    cnt += 1
    # if cnt%50 == 0:
    #     print('Cnt: ' + str(cnt))

# print('Number of viable pairs: ' + str(len(viable_pairs)) + ' in ' + str((datetime.now() - start).total_seconds()))
# for vp in viable_pairs:
#     print(vp)
