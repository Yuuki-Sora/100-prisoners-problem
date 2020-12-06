import random
from cffi.backend_ctypes import xrange

lived = 0
# This value denotes the number of times where everyone lived.
# Since it's an initial value, there's no need to play around with it.

exp_num = 10000
# Change this value to change the number of experiments.

file_name = "HPP-Random-Result.txt"
# This is the output file name.
# Change it to specify a new output file name.

open(file_name, "w").close()

for r in range(exp_num):

    prisoner = range(100)
    # Change this to change the number of prisoners for each round.

    box = random.sample(xrange(0, 100), 100)
    # The declaration of boxes with different numbers inside.

    round_result = 0
    for i in prisoner:
        live = 0
        choice = random.sample(xrange(0, 100), 50)
        for j in choice:
            if box[j] == i:
                live = 1
                break
        if live == 0:
            print(f"Round {r}: prisoner {i} didn't make it. \n")
            break
        if i == len(prisoner) - 1 and live == 1:
            round_result = 1
    if round_result == 1:
        print(f'Round {r}: everyone made it out! \n')
        lived += 1
    with open(file_name, "a") as result:
        result.write(f'{r}:{lived}\n')

print(f'Out of {exp_num} experiments with random choices, number of times where everyone survived: {lived}. ')
print(f'Accumulated data at the end of each round saved to file. ')
