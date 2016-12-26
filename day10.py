
class Bot:
    def __init__(self, bot_id, low_bot, high_bot, low_id=None, high_id=None):
        self.bot_id = bot_id
        self.low_id = low_id
        self.high_id = high_id
        self.low_bot = low_bot
        self.high_bot = high_bot
        self.val_list = []

    def get(self, val):
        self.val_list.append(val)
        if len(self.val_list) > 2:
            print('Too many values!!!')

    def __str__(self):
        txt = 'Bot ' + str(self.bot_id) + ' Low '
        if self.low_bot:
            txt += ' Bot: '
        else:
            txt += ' Out: '

        txt += str(self.low_id) + ' High '

        if self.high_bot:
            txt += ' Bot: '
        else:
            txt += ' Out: '

        txt += str(self.high_id)

        if self.val_list:
            txt += ' Values:'
            for v in self.val_list:
                txt += ' ' + str(v)

        return txt


def set_value(nodes, bot_id, val):
    for n in nodes:
        if n.bot_id == bot_id:
            n.get(val)
            return
    print('Could not find bot: ' + str(bot_id) + ' and set value: ' + str(val))

output_list = {}


def set_output(out_id, val):
    if out_id not in output_list:
        output_list[out_id] = []
    output_list[out_id].append(val)


with open('inputDay10.txt', 'r') as f:
    data = f.readlines()


node_list = []
# Create bot/output list
for d in data:
    if d.startswith('bot'):
        v = d.strip().split(' ')
        b_id = -1
        l_id = None
        h_id = None

        if v[1].isnumeric() and v[6].isnumeric() and v[11].isnumeric():
            b_id = int(v[1])
            l_is_bot = v[5] == 'bot'
            l_id = int(v[6])
            h_is_bot = v[10] == 'bot'
            h_id = int(v[11])
        else:
            print('v[1] ' + v[1] + ' v[6] ' + v[6] + ' v[11] ' + v[11])
            print("Error wrong input: " + d)

        if not b_id == -1:
            node_list.append(Bot(bot_id=b_id, low_bot=l_is_bot, high_bot=h_is_bot, low_id=l_id, high_id=h_id))

# Initialize
for d in data:
    if d.startswith('value'):
        v = d.strip().split(' ')
        if v[1].isnumeric() and v[5].isnumeric():
            b_id = int(v[5])
            val = int(v[1])
            set_value(nodes=node_list, bot_id=b_id, val=val)
        else:
            print("Error wrong input: " + d)


for bot in node_list:
    print('Bots: ' + str(bot))

# Run
valid_output = True
run_count = 0
while valid_output:
    valid_output = False
    run_count += 1

    print('')
    print('#'*20)
    print('# Run ' + str(run_count))
    print('#' * 20)
    for n in node_list:
        if len(n.val_list) == 2:
            n.val_list.sort()
            print('Comparing values: ' + ' '.join(str(x) for x in n.val_list))

            if n.val_list[0] == 2 and n.val_list[1] == 5:
                print('Test Bot ' + str(n.bot_id) + ' is the winner')

            if n.val_list[0] == 17 and n.val_list[1] == 61:
                print('Bot ' + str(n.bot_id) + ' is the winner')

            print('Giving node: ' + str(n.low_id) + ' value: ' + str(n.val_list[0]))
            print('Giving node: ' + str(n.high_id) + ' value: ' + str(n.val_list[1]))
            if n.low_bot:
                set_value(nodes=node_list, bot_id=n.low_id, val=n.val_list[0])
            else:
                set_output(out_id=n.low_id, val=n.val_list[0])

            if n.high_bot:
                set_value(nodes=node_list, bot_id=n.high_id, val=n.val_list[1])
            else:
                set_output(out_id=n.high_id, val=n.val_list[1])

            n.val_list = []
            valid_output = True

print('Type(output_list) ' + str(type(output_list)))
for key, value in output_list.items():
    print('Output ' + str(key) + ": " + str(value))
