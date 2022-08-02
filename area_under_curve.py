from collections import defaultdict

import numpy as np
from sklearn.metrics import auc

xs = []
ys = []

# open file
with open('tests_blank_len_for_graph.log') as file:
    line = 'str'
    while line:
        line = file.readline()
        if line.startswith('maximum length blank space'):
            xs.append(int(line.split(' ')[-1]))
        elif line.startswith('Accuracy'):
            # ys.append(float(line.split(' ')[-1]))
            ys.append(float(line.split(' ')[-1])*100)


# Sort all coordinates in ascending order of xs
xs_and_ys = np.array([xs, ys])
correct_indices = xs_and_ys[0].argsort()
xs_and_ys = xs_and_ys[:, correct_indices]

# Create new list with duplicate xs having ys averaged
# e.g. for xs = [1, 1, 2, 2, 3, 3], ys = [1, 2, 3, 4, 5, 6]
# would become xs = [1, 2, 3] and ys = [1.5, 3.5, 5.5]
total_ys = defaultdict(int)
number_occurerences = defaultdict(int)

for i in range(len(xs_and_ys[0])):
    # add first element to dicts (haven't seen any elements yet)
    if i == 0:
        # use x value as key to store number of occurrences seen and sum of y values
        total_ys[xs_and_ys[0, i]] = xs_and_ys[1, i]
        number_occurerences[xs_and_ys[0, i]] = 1
    else:
        if xs_and_ys[0, i] == xs_and_ys[0, i-1]:
            total_ys[xs_and_ys[0, i]] += xs_and_ys[1, i]
            number_occurerences[xs_and_ys[0, i]] += 1
        else:
            total_ys[xs_and_ys[0, i]] = xs_and_ys[1, i]
            number_occurerences[xs_and_ys[0, i]] = 1


# print(number_occurerences)
# print(total_ys)

final_xs = list(total_ys.keys())
final_ys = []
# divide sum of y values by number of occurrences to get average
for x in final_xs:
    final_ys.append(total_ys[x] / number_occurerences[x])

print('area under curve: ', auc(final_xs, final_ys))
