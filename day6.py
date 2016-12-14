with open('inputDay6.txt', 'r') as f:
    read_data = f.readlines()

char_pos = []
for line in read_data:
    if not char_pos:
        for i in range(0,len(line)):
            char_pos.append('')

    for i in range(0,len(line)):
        char_pos[i] += line[i]

for i in range(0,len(line)):
    distinct_list = list(set(char_pos[i]))
    d = {}
    for c in distinct_list:
        occurences = char_pos[i].count(c)
        d[c] = occurences
    s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=False)]

    print('Pos: ' + str(i) + ' most frequent: ' + str(s[0]))