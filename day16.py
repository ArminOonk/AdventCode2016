# initial_state = '10000'
# file_size = 20
initial_state = '10001110011110000'
file_size = 35651584

state = initial_state

while len(state) < file_size:
    a = state
    b = ''
    for c in reversed(a):
        if c == '1':
            b += '0'
        else:
            b += '1'
    state = a + '0' + b

print('State: ' + state)

# only take what we need
checksum = state[:file_size]

print('Odd/even: ' + str(len(checksum) % 2))
while len(checksum) % 2 == 0:
    new_checksum = ''
    for x in range(0, len(checksum)-1, 2):
        if checksum[x] == checksum[x+1]:
            new_checksum += '1'
        else:
            new_checksum += '0'

    checksum = new_checksum

print('Checksum: ' + checksum)
