with open('inputDay12.txt', 'r') as f:
# with open('testInputDay12.txt', 'r') as f:
    data = f.readlines()

index = 0

reg_a = 0
reg_b = 0
reg_c = 1
reg_d = 0

counter = 0

while True:
    if counter % 10000 == 0:
        print('Index: ' + str(index) + ' a: ' + str(reg_a)  + ' b: ' + str(reg_b)  + ' c: ' + str(reg_c)  + ' d: ' + str(reg_d))
    if index >= len(data):
        break

    if data[index].startswith('cpy'):
        vals = data[index].strip().split()

        if vals[1].isnumeric():
            v = int(vals[1])
        else:
            #register
            if vals[1] == 'a':
                v = reg_a
            elif vals[1] == 'b':
                v = reg_b
            elif vals[1] == 'c':
                v = reg_c
            elif vals[1] == 'd':
                v = reg_d
            else:
                print('Unknown register')

        if vals[2] == 'a':
            reg_a = v
        elif vals[2] == 'b':
            reg_b = v
        elif vals[2] == 'c':
            reg_c = v
        elif vals[2] == 'd':
            reg_d = v
        else:
            print('Unknown register')
        index += 1
    elif data[index].startswith('inc'):
        vals = data[index].strip().split()
        if vals[1] == 'a':
            reg_a += 1
        elif vals[1] == 'b':
            reg_b += 1
        elif vals[1] == 'c':
            reg_c += 1
        elif vals[1] == 'd':
            reg_d += 1
        else:
            print('Unknown register')
        index += 1
    elif data[index].startswith('dec'):
        vals = data[index].strip().split()
        if vals[1] == 'a':
            reg_a -= 1
        elif vals[1] == 'b':
            reg_b -= 1
        elif vals[1] == 'c':
            reg_c -= 1
        elif vals[1] == 'd':
            reg_d -= 1
        else:
            print('Unknown register')
        index += 1
    elif data[index].startswith('jnz'):
        vals = data[index].strip().split()

        if vals[1].isnumeric():
            jump = int(vals[1]) != 0
        else:
            if vals[1] == 'a':
                jump = reg_a != 0
            elif vals[1] == 'b':
                jump = reg_b != 0
            elif vals[1] == 'c':
                jump = reg_c != 0
            elif vals[1] == 'd':
                jump = reg_d != 0
            else:
                print('Unknown register')

        if jump:
            index += int(vals[2])
        else:
            index += 1

    counter += 1


print('Register a: ' + str(reg_a))
print('Register b: ' + str(reg_b))
print('Register c: ' + str(reg_c))
print('Register d: ' + str(reg_d))