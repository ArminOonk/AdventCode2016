class machine:
    def __init__(self, filename, reg_a = 0, reg_b = 0, reg_c = 0, reg_d = 0):
        self.index = 0

        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.reg_d = reg_d

        self.counter = 0

        with open(filename, 'r') as f:
            self.data = f.readlines()

    def state(self):
        txt = 'Index: ' + str(self.index) + "\n"
        txt += 'Reg a: ' + str(self.reg_a)
        txt += ' Reg b: ' + str(self.reg_b)
        txt += ' Reg c: ' + str(self.reg_c)
        txt += ' Reg d: ' + str(self.reg_d) + "\n"

        txt += "Data: \n"
        for d in self.data:
            txt +=  ' ' + d.strip() + "\n"
        txt += '-'*20+"\n"

        return txt

    def get_reg_val(self, reg):
        if reg == 'a':
            return self.reg_a
        if reg == 'b':
            return self.reg_b
        if reg == 'c':
            return self.reg_c
        if reg == 'd':
            return self.reg_d

    def run(self):
        counter = 0

        while True:
            # if counter % 10000 == 0:
            #     print( self.state())
                # print('Data: ')
                # for d in self.data:
                #     print(' ' + d.strip())
                # print('-'*20)

            if self.index >= len(self.data):
                break

            cmd = self.data[self.index].strip()
            print(str(self.index) + ' ' + cmd)
            # print('Counter: ' + str(counter))
            # print('Command: ' + cmd)

            # if counter == 1000:
            #     quit()

            if cmd.startswith('cpy'):
                self.cpy(cmd)
            elif cmd.startswith('inc'):
                # Check if we can optimize this a bit
                if self.index + 4 < len(self.data) and self.index - 1 >= 0 and \
                   self.data[self.index-1].startswith('cpy') and \
                   self.data[self.index + 1].startswith('dec') and \
                   self.data[self.index + 2].startswith('jnz') and \
                   self.data[self.index + 3].startswith('dec') and \
                   self.data[self.index + 3].startswith('jnz'):

                    cpysrc, cpydest = self.data[self.index-1].split(" ")[1:]
                    dec1op = self.data[self.index+1].split(" ")[1]
                    jnz1cond, jnz1off = self.data[self.index+2].split(" ")[1:]
                    dec2op = self.data[self.index+3].split(" ")[1]
                    jnz2cond, jnz2off = self.data[self.index+4].split(" ")[1:]

                    if cpydest == dec1op and dec1op == jnz1cond and \
                        dec2op == jnz2cond and \
                        jnz1off == "-2" and jnz2off == "-5":

                        vals = cmd.split()
                        if vals[1] == 'a':
                            self.reg_a = self.get_reg_val(cpysrc)* self.get_reg_val(dec2op)
                        elif vals[1] == 'b':
                            self.reg_b = self.get_reg_val(cpysrc)* self.get_reg_val(dec2op)
                        elif vals[1] == 'c':
                            self.reg_c = self.get_reg_val(cpysrc)* self.get_reg_val(dec2op)
                        elif vals[1] == 'd':
                            self.reg_d = self.get_reg_val(cpysrc)* self.get_reg_val(dec2op)

                        self.index += 5
                        print('Optimize!')
                        continue
                else:
                    self.inc(cmd)
            elif cmd.startswith('dec'):
                self.dec(cmd)
            elif cmd.startswith('jnz'):
                self.jnz(cmd)
            elif cmd.startswith('tgl'):
                self.tgl(cmd)
            else:
                print('Unknown command!')
                break

            # print('State: ' + self.state())
            # print('Data: ')
            # for d in self.data:
            #     print(' ' + d.strip())
            # print('-'*20)
            counter += 1

    def cpy(self, cmd):
        vals = cmd.split()

        try:
            v = int(vals[1])
        except ValueError:
            # register
            if vals[1] == 'a':
                v = self.reg_a
            elif vals[1] == 'b':
                v = self.reg_b
            elif vals[1] == 'c':
                v = self.reg_c
            elif vals[1] == 'd':
                v = self.reg_d
            else:
                print('Unknown register')

        if vals[2] == 'a':
            self.reg_a = v
        elif vals[2] == 'b':
            self.reg_b = v
        elif vals[2] == 'c':
            self.reg_c = v
        elif vals[2] == 'd':
            self.reg_d = v

        self.index += 1

    def inc(self, cmd):
        vals = cmd.split()
        if vals[1] == 'a':
            self.reg_a += 1
        elif vals[1] == 'b':
            self.reg_b += 1
        elif vals[1] == 'c':
            self.reg_c += 1
        elif vals[1] == 'd':
            self.reg_d += 1
        else:
            print('Unknown register')

        self.index += 1

    def dec(self, cmd):
        vals = cmd.split()
        if vals[1] == 'a':
            self.reg_a -= 1
        elif vals[1] == 'b':
            self.reg_b -= 1
        elif vals[1] == 'c':
            self.reg_c -= 1
        elif vals[1] == 'd':
            self.reg_d -= 1
        else:
            print('Unknown register')

        self.index += 1

    def jnz(self, cmd):
        vals = cmd.split()

        if vals[1].isnumeric():
            jump = int(vals[1]) != 0
        else:
            if vals[1] == 'a':
                jump = self.reg_a != 0
            elif vals[1] == 'b':
                jump = self.reg_b != 0
            elif vals[1] == 'c':
                jump = self.reg_c != 0
            elif vals[1] == 'd':
                jump = self.reg_d != 0
            else:
                print('Unknown register')

        if jump:
            try:
                dist = int(vals[2])
            except ValueError:
                if vals[2] == 'a':
                    dist = self.reg_a
                elif vals[2] == 'b':
                    dist = self.reg_b
                elif vals[2] == 'c':
                    dist = self.reg_c
                elif vals[2] == 'd':
                    dist = self.reg_d
                else:
                    print('Unknown distance: ' + vals[2])
            self.index += dist
        else:
            self.index += 1

    def tgl(self, cmd):
        vals = cmd.split()

        try:
            par = int(vals[1])
        except ValueError:
            if vals[1] == 'a':
                par = self.reg_a
            elif vals[1] == 'b':
                par = self.reg_b
            elif vals[1] == 'c':
                par = self.reg_c
            elif vals[1] == 'd':
                par = self.reg_d
            else:
                print('Unknown register')

        target_index = self.index + par

        if target_index >= 0 and target_index < len(self.data):
            target_cmd = self.data[target_index]
            tcv = target_cmd.strip().split()

            if len(tcv) == 2:
                if tcv[0] == 'inc':
                    self.data[target_index] = 'dec ' + tcv[1]
                else:
                    self.data[target_index] = 'inc ' + tcv[1]
            elif len(tcv) == 3:
                new_command = ''

                if tcv[0] == 'jnz':
                    new_command = 'cpy ' + tcv[1] + ' ' + tcv[2]
                else:
                    new_command = 'jnz ' + tcv[1] + ' ' + tcv[2]

                # print('New command: ' + new_command)
                self.data[target_index] = new_command
            else:
                print('Unknown target command: ' + tcv)

        self.index += 1

# mach = machine('inputDay23.txt', reg_a=7)
mach = machine('inputDay23.txt', reg_a=12)
mach.run()
print(mach.state())
