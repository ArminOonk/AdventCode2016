def read_room(txt):
    index = txt.rfind('-')

    name = txt[:index]
    rest = txt[(index + 1):]

    index_checksum = rest.find('[')

    sector_id = int(rest[:index_checksum])
    checksum = rest[(index_checksum + 1):(index_checksum + 1) + 5]

    return {'name':name, 'sector_id':sector_id, 'checksum':checksum}


def decrypt(room):
    key = room['sector_id'] % 26
    output = ''
    for c in room['name']:
        if c == '-':
            output += ' '
        else:
            output += chr(ord('a') + ((ord(c) - ord('a')) + key ) % 26)
    return output


def is_valid_room(room):
    distinct_list = list(set(room['name']))
    distinct_list.remove('-')
    # print('Distinct list: ')

    d = {}
    for c in distinct_list:
        occurences = room['name'].count(c)
        # print(c + ' occured ' + str(occurences))
        d[c] = occurences

    sorted_occ = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    # sorted_occ = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]

    # for key,value in sorted_occ:
    #     print(key + ' occured: ' + str(value))

    calc_checksum = ''
    for key,value in sorted_occ:
        calc_checksum += key
        if len(calc_checksum) >= 5:
            break

    # print('Received checksum ' + room['checksum'] + ' calculated checksum ' + calc_checksum)
    return room['checksum'] == calc_checksum


# txt = 'aaaaa-bbb-z-y-x-123[abxyz]'
# x = read_room(txt)

with open('inputDay4.txt', 'r') as f:
    read_data = f.readlines()

sector_id_sum = 0
for txt in read_data:
    x = read_room(txt)
    # print('Name: ' + x['name'] + ' sector id: ' + str(x['sector_id']) + ' checksum: ' + x['checksum'] + ' is valid: ' + str(is_valid_room(x)))
    if is_valid_room(x):
        sector_id_sum += x['sector_id']

        txt_dec = decrypt(x)
        #print('sector id: ' + str(x['sector_id']) + " " + txt_dec)

        if 'north' in txt_dec:
            print('sector id: ' + str(x['sector_id']) + " " + txt_dec)


print('Sum sector ids: ' + str(sector_id_sum))



