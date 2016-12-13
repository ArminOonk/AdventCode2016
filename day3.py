def is_triangle_list(l):
    return is_triangle(l[0], l[1], l[2])


def is_triangle(v1, v2, v3):
    return v1 + v2 > v3 and v2 + v3 > v1 and v3 + v1 > v2


def read_line(l):
    v = l.split(' ')
    v = list(filter(None, v))
    v = [float(i) for i in v]
    return v


with open('inputDay3.txt', 'r') as f:
    read_data = f.readlines()

tested_triangle = 0
possible_triangle = 0
#for l in read_data:
for ii in range(0, len(read_data), 3):
    l = read_data[ii]

    vals = []
    for j in range(0,3):
        v = read_line(read_data[ii+j])
        print("length " + str(len(v)) + " " + str(v[0]) + " " + str(v[1]) + " " + str(v[2]))
        vals.append(v)

    for a in range(0,3):
        v1 = vals[0][a]
        v2 = vals[1][a]
        v3 = vals[2][a]

        print('Reordered: ' + str(v1) + " "+ str(v2) + " "+ str(v3))
        tested_triangle += 1
        if is_triangle(v1, v2 , v3):
            possible_triangle += 1
        else:
            print("Impossible triangle!")


print("There are " + str(possible_triangle) + ' possible from a total of ' + str(tested_triangle))