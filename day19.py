class elf:
    def __init__(self, id):
        self.id = id
        self.next = None
        self.prev = None

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev


nr_of_elves = 3014603
# nr_of_elves = 5
elves = []

for x in range(0, nr_of_elves):
    elves.append(elf(x+1))

for x in range(0, nr_of_elves):
    elves[x].prev = elves[(x-1) % nr_of_elves]
    elves[x].next = elves[(x+1) % nr_of_elves]

start = elves[0]
mid = elves[int(0.5*nr_of_elves)]

for x in range(0, nr_of_elves):
    mid.delete()
    mid = mid.next

    if (nr_of_elves-x) % 2 == 1:
        mid = mid.next
    start = start.next

print('Elf: ' + str(start.id))
quit()

nr_elves_with_present = nr_of_elves
index = 0

while nr_elves_with_present != 1:
    if elves[index]:
        # We are still playing
        # Find the next elf with presents

        middle = int(0.5*nr_elves_with_present)
        tmp_index = index

        # print('Middle: ' + str(middle) + ' tmp_index: ' + str(tmp_index))

        while middle:
            if elves[tmp_index]:
                middle -= 1
            tmp_index = (tmp_index + 1) % nr_of_elves

        # print('Middle elf: ' + str(tmp_index))
        for x in range(1, nr_of_elves):

            if elves[tmp_index]:
                # Steal!
                elves[index] += elves[tmp_index]
                elves[tmp_index] = 0
                nr_elves_with_present -= 1

                if nr_elves_with_present % 10000 == 0:
                    print('Elves remaining: ' + str(nr_elves_with_present))
                # print(elves)
                break
            tmp_index = (tmp_index + 1) % nr_of_elves

    index += 1
    index %= nr_of_elves


print('Elf with all the presents: ' + str(index))