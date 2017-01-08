import itertools

def swap_position(txt, x, y, reverse=False):
    if x < y:
        low = x
        high = y
    else:
        low = y
        high = x
    return txt[:low] + txt[high] + txt[low+1:high] + txt[low] + txt[high+1:]


def swap_letter(txt, x, y, reverse=False):
    txt = txt.replace(x, '!')
    txt = txt.replace(y, x)
    txt = txt.replace('!', y)
    return txt


def reverse_position(txt, x, y, reverse=False):
    if x < y:
        low = x
        high = y
    else:
        low = y
        high = x

    rev_str = txt[low:high+1]

    return txt[:low] + rev_str[::-1] + txt[high+1:]


def rotate_left(txt, steps, reverse=False):
    if reverse:
        return rotate_right(txt, steps, False)

    for i in range(0, steps):
        txt = txt[1:] + txt[0]
    return txt


def rotate_right(txt, steps, reverse=False):
    if reverse:
        return rotate_left(txt, steps, False)

    for i in range(0, steps):
        txt = txt[-1] + txt[:len(txt)-1]
    return txt


def rotate_on_letter(txt, x, reverse=False):
    index = txt.find(x)

    rotations = index + 1

    if index >= 4:
        rotations += 1
    return rotate_right(txt, rotations)


def move_position(txt, x, y, reverse=False):
    ret = txt[:x] + txt[x+1:]
    # print('ret: ' + ret)
    # if y == 0:
    #     return txt[x] + ret
    return ret[:y] + txt[x] + ret[y:]


def hash_password(password, data):
    for d in data:
        if d.startswith('swap position'):
            vals = d.split(' ')
            x = int(vals[2])
            y = int(vals[5])
            password = swap_position(password, x, y)
            # print('Swapping position: ' + str(x) + ' ' + str(y) + ' result: ' + password)
        elif d.startswith('swap letter'):
            vals = d.split(' ')
            x = vals[2].strip()
            y = vals[5].strip()
            password = swap_letter(password, x, y)
            # print('Swapping letter: ' + x + ' ' + y + ' result: ' + password)
        elif d.startswith('rotate based on position of letter'):
            vals = d.split(' ')
            x = vals[6].strip()
            password = rotate_on_letter(password, x)
            # print('Rotate based on letter ' + x + ' result: ' + password)
        elif d.startswith('rotate'):
            vals = d.split(' ')
            rot = int(vals[2])
            if vals[1] == 'left':
                password = rotate_left(password, rot)
                # print('Rotating left nr steps ' + str(rot) + ' result: ' + password)
            elif vals[1] == 'right':
                password = rotate_right(password, rot)
                # print('Rotating right nr steps ' + str(rot) + ' result: ' + password)
            else:
                print('Unknown rotation')
        elif d.startswith('move position'):
            vals = d.split(' ')
            x = int(vals[2])
            y = int(vals[5])
            password = move_position(password, x, y)
            # print('Moving position ' + str(x) + ' with: ' + str(y) + ' result: ' + password)
        elif d.startswith('reverse positions'):
            vals = d.split(' ')
            x = int(vals[2])
            y = int(vals[4])
            password = reverse_position(password, x, y)
            # print('Reversing position ' + str(x) + ' and ' + str(y) + ' result: ' + password)
        else:
            print('Unknown command: ' + d)
    return password


with open('inputDay21.txt', 'r') as f:
    data = f.readlines()

# password = 'abcde'
password = 'abcdefgh'
print('Password: ' + password + ' hash: ' + hash_password(password, data))

hash_to_find = 'fbgdceah'

per = itertools.permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# print('Number of permutations: ' + str(len(per)))

cnt = 0
for p in per:
    password = ''.join(p)
    h = hash_password(password, data)

    if h == hash_to_find:
        print('Found hash, password: ' + password + ' hash: ' + hash_to_find)

    cnt += 1
    if cnt%1000 == 0:
        print(cnt)
#     print(''.join(p))

