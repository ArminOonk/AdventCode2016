def swap_position(txt, x, y):
    if x < y:
        low = x
        high = y
    else:
        low = y
        high = x
    return txt[:low] + txt[high] + txt[low+1:high] + txt[low] + txt[high+1:]


def swap_letter(txt, x, y):
    txt = txt.replace(x, '!')
    txt = txt.replace(y, x)
    txt = txt.replace('!', y)
    return txt


def reverse_position(txt, x, y):
    if x < y:
        low = x
        high = y
    else:
        low = y
        high = x

    rev_str = txt[low:high+1]

    return txt[:low] + rev_str[::-1] + txt[high+1:]


def rotate_left(txt, steps):
    for i in range(0, steps):
        txt = txt[1:] + txt[0]
    return txt


def rotate_right(txt, steps):
    for i in range(0, steps):
        txt = txt[-1] + txt[:len(txt)-1]
    return txt


def rotate_on_letter(txt, x):
    index = txt.find(x)

    rotations = index + 1

    if index >= 4:
        rotations += 1
    return rotate_right(txt, rotations)


def move_position(txt, x, y):
    ret = txt[:x] + txt[x+1:]
    if y == 0:
        return txt[x] + ret
    return ret[:y] + txt[x] + ret[y+1:]


with open('inputDay21.txt', 'r') as f:
    data = f.readlines()

password = 'abcde'

password = swap_position(password, 4, 0)
print('Swap position 4, 0: ' + password)

password = swap_letter(password, 'd', 'b')
print("Swap letter 'd' 'b': " + password)

password = reverse_position(password, 0, 4)
print('Reverse position 0 4: ' + password)

password = rotate_left(password, 1)
print("Rotate left: " + password)

# password = rotate_right(password, 2)
# print("Rotate right: " + password)

password = move_position(password, 1, 4)
print('Move position 1 to 4: ' + password)

password = move_position(password, 3, 0)
print('Move position 3 to 0: ' + password)

password = rotate_on_letter(password, 'b')
print("Rotate on letter b: " + password)

password = rotate_on_letter(password, 'd')
print("Rotate on letter d: " + password)
