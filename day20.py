def is_excluded(ex_list, i):
    for excluded_range in ex_list:
        if i >= excluded_range['min'] and i <= excluded_range['max']:
            i = excluded_range['max']
            return True, i
    return False, i


with open('inputDay20.txt', 'r') as f:
    data = f.readlines()

excl_list = []
for d in data:
    vals = d.split('-')
    excl_list.append({'min': int(vals[0]), 'max': int(vals[1])})
#
# excl_list.append({'min': 0, 'max': 0})
# excl_list.append({'min': 4294967295, 'max': 4294967295})

excl_list_sort = sorted(excl_list, key=lambda k: (k['min'], k['max']))

min_val = 0
nr_valid = 0

i = 0
valid_options = 0
while i <= 4294967295:
    is_excl, i = is_excluded(excl_list_sort, i)

    if not is_excl:
        valid_options += 1
        
    i += 1
    if valid_options % 10000 == 0:
        print('Options found: ' + str(valid_options) + ' searching at: ' + str(i))

print('valid options: ' + str(valid_options))
quit()

def reduce(list_val):

    cur_min = 0
    cur_max = 0
    reduced_list = []

    for ex in list_val:
        if cur_min == cur_max:
            # Looking for the start of a range
            cur_min = ex['min']
            cur_max = ex['max']
        else:

            if ex['min'] >= cur_min and ex['min'] <= cur_max:
                # This falls in a valid range
                cur_max = ex['max']
            else:
                # We have found a range
                reduced_list.append({'min': cur_min, 'max': cur_max})
                # Start a new one
                cur_min = ex['min']
                cur_max = ex['max']
    return reduced_list

prev_length = len(excl_list_sort)
reduced_list = []

while prev_length != len(reduced_list):
    prev_length = len(reduced_list)
    reduced_list = reduce(excl_list_sort)
    print('Reduce')

# reduced_list = reduce(excl_list_sort)

nr_valid_ip = 4294967295

for rl in reduced_list:
    print(str(rl['max']) + ' - ' + str(rl['min']) + ' = ' + str(rl['max'] - rl['min']))
    nr_valid_ip -= rl['max'] - rl['min']

#
# for ex in range(0, len(excl_list_sort)):
#     if min_val >= excl_list_sort[ex]['min'] and min_val <= excl_list_sort[ex]['max']:
#         min_val = excl_list_sort[ex]['max'] + 1
#
#     if excl_list_sort[ex]['min'] >= cur_min and excl_list_sort[ex]['min'] <= cur_max:
#         # The minimum value is in the current list
#         if excl_list_sort[ex]['max'] > cur_max:
#             # This maximum is bigger, this is our new current max
#             cur_max = excl_list_sort[ex]['max']
#     else:
#         if cur_min != cur_max:
#             print('Appending: ' + str(cur_min) + ' ' + str(cur_max))
#             reduced_list.append({'min': cur_min, 'max': cur_max})
#             cur_min = cur_max
#
#     # print(str(excl_list_sort[ex]['min']) + ', ' + str(excl_list_sort[ex]['max']))
#     if ex:
#         nr = excl_list_sort[ex-1]['max'] - excl_list_sort[ex]['min'] - 2
#         # print(str(excl_list_sort[ex-1]['max']) + ', ' + str(excl_list_sort[ex]['min']) + ' nr: ' + str(nr))
#         if nr > 0:
#             nr_valid += nr
#     else:
#         print(str(excl_list_sort[ex]['min']) + ', ' + str(excl_list_sort[ex]['max']))

print('Min val: ' + str(min_val))
print('Number of valid ip: ' + str(nr_valid))

print('Length input: ' + str(len(excl_list_sort)))
print('Reduced length: ' + str(len(reduced_list)))
print('Reduced valid: ' + str(nr_valid_ip))

print('Lowest: ' + str(excl_list_sort[0]))
print('Lowest: ' + str(excl_list_sort[1]))
print('Lowest: ' + str(excl_list_sort[2]))

print('Reduced: ' + str(reduced_list[0]))
print('Reduced: ' + str(reduced_list[1]))
print('Reduced: ' + str(reduced_list[2]))
