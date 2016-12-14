import hashlib

# door_id = 'abc'
door_id = 'uqwqemis'
password = ['_', '_', '_', '_', '_', '_', '_', '_']

i = 0
while(True):
    i += 1

    if i % 1000000 == 0:
        print(i)

    m = hashlib.md5()
    m.update(bytes(door_id+str(i), 'utf-8'))
    h = m.hexdigest()

    if h.startswith('00000'):
        pos = int(h[5], 16)
        print('pos: ' + str(pos) + ' Possible match: ' + str(i) + ' md5(' + door_id + str(i) + ') = ' + h)
        if pos >= 0 and pos <= 7 and password[pos] == '_':
            password[pos] = h[6]
            print(str(i) + ' md5(' + door_id + str(i) + ') = ' + h + ' password: ' + ''.join(password))



    if not '_' in password:
        break

print('password: ' + ''.join(password))