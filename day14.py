import hashlib


def find_repeat(txt, count):
    for x in range(0, len(txt) - count):
        if txt[x:x+count] == txt[x]*count:
            return txt[x:x+count]
    return ''


def is_quintet(txt, pat):
    return find_repeat(txt, 5) == 5*pat


def get_hash(txt, repeat):
    m = hashlib.md5()
    m.update(bytes(txt, 'utf-8'))
    h = m.hexdigest()

    for x in range(0, repeat):

        m1 = hashlib.md5()
        m1.update(bytes(h, 'utf-8'))
        h = m1.hexdigest()

    return h


# salt = 'abc'
stretch = 2016
salt = 'ngcjuoqr'
keys = []
index = 0

# hashes = []
# for x in range(0,40000):
#     if x%1000 == 0:
#         print('x: ' + str(x))
#     h = get_hash(salt + str(x), stretch)
#     hashes.append(h)
#
# with open('hashes.txt', 'w') as f:
#     f.write("\n".join(hashes)+"\n")
#
# quit()

with open('hashes.txt', 'r') as f:
    hashes = f.readlines()

while len(keys) < 64:
    h = hashes[index]

    rep = find_repeat(h, 3)
    if rep:
        for x in range(1, 1000):
            h2 = hashes[index+x]

            if is_quintet(h2, rep[0]):
                keys.append(index)
                print('Keys found: ' + str(len(keys)))
                break
    index += 1

print(keys)
print('answer: ' + str(keys[-1]))

# quit()
# while len(keys) < 63:
#     h = get_hash(salt+str(index), stretch)
#
#     rep = find_repeat(h, 3)
#     if rep:
#         # print(str(index) + ' ' + rep + ' ' + h)
#
#         for x in range(1, 1000):
#             h2 = get_hash(salt+str(index+x), stretch)
#
#             if is_quintet(h2, rep[0]):
#                 keys.append(index)
#                 print('Keys found: ' + str(len(keys)))
#                 break
#
#     index += 1
# # print('md5: ' + h)
# # print('Repeat: ' + find_repeat(h, 3))
# print(keys)
# print('answer: ' + str(keys[-1]))
