import sys
import time

import numpy as np

from knn_levenshtein import KNearestLevenshtein
from species import hide_random_sequence, missing_values_array, open_file
from tests import calcAccuracy

log_file = open("all_mus_acc.log", 'w')
sys.stdout = log_file

# reading the common genes file to see which genes can be used for imputation
# common_genes = open('genes_in_both.txt', 'r')
# data = common_genes.read()
# common_genes_list = data.split('\n')
# common_genes_list = ['Mis12', 'Mis18a', 'Mis18bp1', 'Misp', 'Mitd1', 'Mitf']
common_genes_list = ['Mis12', 'Mis18a', 'Mis18bp1', 'Misp', 'Mitd1']

char_limit = 200000

acc_rates = []
times = []

# for i in range(7397, 7398):
for i in range(len(common_genes_list)):
    start_time = time.time()

    mus_path = 'all mouse genes/musculus/' + common_genes_list[i] + '.fna'
    pah_path = 'all mouse genes/pahari/' + common_genes_list[i] + '.fna'

    genomeList = open_file(mus_path, character_limit=char_limit)
    genome = ''.join(genomeList)  # combine each line of genome into 1 string
    genome = genome.replace('\n', '')  # remove newline characters

    otherGenomeList = open_file(pah_path, character_limit=char_limit)
    otherGenome = ''.join(otherGenomeList)
    otherGenome = otherGenome.replace('\n', '')  # remove newline characters

    new_genome = hide_random_sequence(genome)
    correct_values = missing_values_array(genome, new_genome)

    kn = KNearestLevenshtein()
    kn.fit(new_genome)
    preds = kn.predict(otherGenome)

    amount_time = time.time() - start_time

    print('\nPRED DETAILS FOR: ' + common_genes_list[i])
    print('time: %s' % amount_time)

    times.append(amount_time)
    acc_rates.append(calcAccuracy(correct_values, preds))

print('\nAVERAGE ACCURACY: ', np.mean(acc_rates))
print('TOTAL TIME: ', np.sum(times))
