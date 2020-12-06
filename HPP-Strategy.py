import random
from cffi.backend_ctypes import xrange

lived = 0
# This value denotes the number of times where everyone lived.
# Since it's an initial value, there's no need to play around with it.

exp_num = 10000
# Change this value to change the number of experiments.

file_name = "HPP-Strategy-Result.txt"
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
        choice = i
        for j in range(50):
            if box[choice] == i:
                live = 1
                break
            else:
                choice = box[choice]
        if live == 0:
            print(f"Round {r}: prisoner {i} didn't make it. \n")
            break
        if i == len(prisoner) - 1 and live == 1:
            round_result = 1
    if round_result == 1:
        print(f'Round {r}: everyone made it out! \n')
        lived += 1
    with open(file_name, "a") as result:
        result.write(f'{r}:{100*lived/(r+1)}%\n')

print(f'Out of {exp_num} experiments with our new strategy, number of times where everyone survived: {lived}. ')
print(f'Total survival rate of all experiments: {100*lived/exp_num}%. ')
# This program outputs the survival rate instead, so it is easier to generate a graph with the output file.
print(f'Accumulated data at the end of each round saved to file. ')
