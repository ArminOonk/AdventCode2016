def contains_abba(l):
    for i in range(0, len(l) - 3):
        if is_abba(l[i:i + 4]):
            return True

    return False

def is_abba(l):
    return l[:2] == l[:1:-1] and l[0] != l[1]


def is_tls(net_list, hyper_list):
    for hl in hyper_list:
        if contains_abba(hl):
            return False

    for nl in net_list:
        if contains_abba(nl):
            return True
    return False


def extract_nets(l):
    net_list = []
    hyper_list = []
    while True:
        try:
            first_index = l.index('[')
        except ValueError:
            first_index = len(l)
        net_list.append(l[:first_index])

        try:
            second_index = l.index(']')
            hyper_list.append((l[(first_index + 1):second_index]))
            l = l[(second_index + 1):]
        except ValueError:
            break
    return net_list, hyper_list

with open('inputDay7.txt', 'r') as f:
    read_data = f.readlines()

number_of_tls = 0
for l in read_data:
    nl ,hl = extract_nets(l.strip())

    if is_tls(net_list=nl, hyper_list=hl):
        print(l + " is TLS")
        number_of_tls += 1

print('Number of TLS: ' + str(number_of_tls))