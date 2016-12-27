class State:
    def __init__(self):
        self.elevator = 1
        self.floor = {1:[], 2:[], 3:[], 4:[]}

    def __str__(self):
        txt = 'Elevator is at floor ' + str(self.elevator)
        for key, value in self.floor.items():
            txt += ' floor ' + str(key) + ": "
            if value:
                for v in value:
                    txt += ' ' + str(v)
            else:
                txt += 'Empty'
        return txt

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
                print('ui: ' + ui)
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

    """
    Options for the next state are
    - Go up one floor, go down one floor
    - Move with 1 item
    - Move with 2 items

    """
    def next_states(self):
        ret = []
        t = ''
        for x in self.floor[self.elevator]:
            t += ' ' + str(x)
        print('Items on this floor: ' + t)
        return ret
"""
We can stop a particular branch if:
- We reached the end state, everything on the 4th floor
- We do not have a next_state
- This particular state has been reached before with less steps
"""
initial_state = State()
initial_state.floor[1].append('HM')
initial_state.floor[1].append('LM')
initial_state.floor[2].append('HG')
initial_state.floor[3].append('LG')
initial_state.elevator = 1


print(initial_state)
print('Initial state is safe: ' + str(initial_state.is_safe()))
initial_state.next_states()

