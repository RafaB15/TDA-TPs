import random

def write_random_numbers(filename, num_numbers):
    with open(filename, 'w') as file:
        file.write("{}".format(num_numbers) + '\n\n')

        for _ in range(num_numbers):
            random_number = round(random.random(), 3)
            file.write(str(random_number) + '\n')

for i in range(1, 26):
    for j in range(1, 4):
        write_random_numbers("testing/amount_{}_version_{}.txt".format(i, j), i)
