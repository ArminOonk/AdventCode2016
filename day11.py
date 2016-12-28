from copy import deepcopy
from datetime import datetime
"""
To do build a tree like structure
"""


def combinations(l):
    ret = []
    if len(l) < 2:
        return ret

    if len(l) == 2:
        return [(l[0], l[1])]

    for x in range(0, len(l) - 1):
        for y in range(x+1, len(l)):
            r = (l[x], l[y])
            ret.append(r)
    return ret


class State:
    def __init__(self):
        self.elevator = 1
        self.floor = {1:[], 2:[], 3:[], 4:[]}

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        txt = 'Elevator is at floor ' + str(self.elevator)
        for key, value in self.floor.items():
            txt += ' floor ' + str(key) + ": "
            if value:
                # value.sort()
                for v in value:
                    txt += ' ' + str(v)
            else:
                txt += 'Empty'
        return txt

    def move_up(self, name):
        for key, value in self.floor.items():
            for v in value:
                if v == name:
                    if key+1 > 4:
                        print('Illegal move, going to floor 5')
                        return False
                    # Move this item up
                    self.floor[key+1].append(name)
                    self.floor[key].remove(name)
                    return True
        return False

    def move_down(self, name):
        for key, value in self.floor.items():
            for v in value:
                if v == name:
                    if key-1 < 1:
                        print('Illegal move, going to floor 0')
                        return False
                    # Move this item up
                    self.floor[key-1].append(name)
                    self.floor[key].remove(name)
                    return True
        return False
    """
    Test if this a safe state

    """
    def is_safe(self):
        for key, value in self.floor.items():
            if len(value) <= 1:
                continue

            # We got multiple items lets check the combinations
            # Find the first microchip
            chip_list = []
            gen_list = []
            for ui in value:
                if ui[1] == 'M':
                    chip_list.append(ui)
                if ui[1] == 'G':
                    gen_list.append(ui)

            if not chip_list:
                continue  # No chips it is safe

            if not gen_list:
                continue  # No generators we are safe

            for cl in chip_list:
                has_own_gen = False
                potential_danger = False
                for gl in gen_list:
                    if cl[0] == gl[0]:
                        # We have found a safe combination
                        has_own_gen = True
                        continue # Go to the next chip
                    else:
                        potential_danger = True
                if potential_danger and not has_own_gen:
                    return False
        return True

    def is_end_state(self):
        if not self.floor[1] and not self.floor[2] and not self.floor[3] and self.floor[4]:
            return True
        return False
    """
    Options for the next state are
    - Go up one floor, go down one floor
    - Move with 1 item
    - Move with 2 items

    """
    def next_states(self):
        ret = []

        items_on_floor = self.floor[self.elevator]

        # print('Items on the floor: ' + str(items_on_floor))
        # First do all single item moves, only keep valid end result
        for i in items_on_floor:
            if self.elevator < 4:
                new_state = deepcopy(self)
                new_state.move_up(i)
                new_state.elevator += 1
                if new_state.is_safe():
                    ret.append(new_state)
            if self.elevator > 1:
                new_state = deepcopy(self)
                new_state.move_down(i)
                new_state.elevator -= 1
                if new_state.is_safe():
                    ret.append(new_state)

        dl = combinations(items_on_floor)

        # Do all double item moves, only keep valid end result
        for d1, d2 in dl:
            if d1 == d2:
                print('Items should not appear twice')
                continue  # Same item twice, impossible

            if len(d1) != 2 or len(d2) != 2:
                print('Invalid length! in devices ' + self.__str__())
                print(dl)
                quit()

            if d1[1] != d2[1] and d1[0] != d2[0]:
                # one is generator other is chip and they are not of the same type, UNSAFE
                continue

            # print('This move is possible')
            if self.elevator < 4:
                new_state = deepcopy(self)
                new_state.move_up(d1)
                new_state.move_up(d2)
                new_state.elevator += 1
                if new_state.is_safe():
                    ret.append(new_state)

            if self.elevator > 1:
                new_state = deepcopy(self)
                new_state.move_down(d1)
                new_state.move_down(d2)
                new_state.elevator -= 1
                if new_state.is_safe():
                    ret.append(new_state)
        return ret
"""
We can stop a particular branch if:
- We reached the end state, everything on the 4th floor
- We do not have a next_state
- This particular state has been reached before with less steps
"""
# Test state
initial_state = State()
initial_state.floor[1].append('HM')
initial_state.floor[1].append('LM')
initial_state.floor[2].append('HG')
initial_state.floor[3].append('LG')
initial_state.elevator = 1

# Real state
# initial_state = State()
# initial_state.floor[1].append('SG')
# initial_state.floor[1].append('SM')
# initial_state.floor[1].append('PG')
# initial_state.floor[1].append('PM')
#
#
# initial_state.floor[2].append('TG')
# initial_state.floor[2].append('RG')
# initial_state.floor[2].append('RM')
# initial_state.floor[2].append('CG')
# initial_state.floor[2].append('CM')
#
# initial_state.floor[3].append('TM')
# initial_state.elevator = 1

print(initial_state)
# print('Initial state is safe: ' + str(initial_state.is_safe()))
# print('Initial state is end state: ' + str(initial_state.is_end_state()))

steps = 1
tree = {}
tree.update({steps: [initial_state]})

start_time = datetime.now()
while True:
    cur_state = tree[steps]
    tmp = []
    for cs in cur_state:
        tmp += cs.next_states()

    # Clean up state
    # remove states which are found before

    new_states = []
    for t in tmp:
        if t not in new_states:
            new_states.append(t)

    for x in range(1, steps):
        for old_state in tree[x]:
            for ns in new_states:
                if ns == old_state:
                    new_states.remove(ns)

    # Check if we reached the end state
    for ns in new_states:
        if ns.is_end_state():
            print('End state reached in ' + str(steps) + ' steps')
            print('Search took: ' + str((datetime.now() - start_time).total_seconds()) + ' sec')
            quit()

    print('Step: ' + str(steps) + ' Found ' + str(len(new_states)) + ' new states')
    # for ns in new_states:
    #     print('new state content: ' + str(ns))
    steps += 1

    tree.update({steps: new_states})
    if steps > 20:
        print('Too many steps, stopping')
        break

print('Search took: ' + str((datetime.now() - start_time).total_seconds()) + ' sec')