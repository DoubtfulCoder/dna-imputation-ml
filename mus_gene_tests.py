import sys
import time

import numpy as np

from knn_levenshtein import KNearestLevenshtein
from species import hide_random_sequence, missing_values_array, open_file

# from tests import calcAccuracy

log_file = open("all_mus_acc.log", 'w')
sys.stdout = log_file


# moved this into here from tests.py since it allows output
# to be seen in log file without waiting for all code to finish
def calcAccuracy(correct_values, preds):
    num_correct = 0
    num_total = 0
    error_rates = []
    for i in range(len(correct_values)):
        correct = correct_values[i]
        pred = preds[i]
        error_rates.append(
            KNearestLevenshtein.levenshteinDistanceCalc(correct, pred)/len(pred))
        for j in range(len(correct)):
            if correct[j] == pred[j]:
                num_correct += 1
            num_total += 1
    print('Accuracy: ', num_correct/num_total)
    print('Levenshtein Error: ', np.mean(error_rates))
    return num_correct/num_total


# reading the common genes file to see which genes can be used for imputation
# common_genes = open('genes_in_both.txt', 'r')
common_genes = open('genes_in_all.txt', 'r')
data = common_genes.read()
common_genes_list = data.split('\n')
# common_genes_list = ['Mis12', 'Mis18a', 'Mis18bp1', 'Misp', 'Mitd1', 'Mitf']
# common_genes_list = ['Mis12', 'Mis18a', 'Mis18bp1', 'Misp', 'Mitd1']

char_limit = 200000

acc_rates = []
times = []
idx = []
# for i in range(len(common_genes_list)):
# for i in range(3, 6):
i = 0
# while(i < 2):
#     rand = np.random.randint(0, 14391)
#     if rand in idx:
#         i -= 1
#         continue
#     idx.append(rand)
for rand in [0,3,4,5]:
    start_time = time.time()

    mus_path = 'all mouse genes/musculus/' + common_genes_list[rand] + '.fna'
    pah_path = 'all mouse genes/pahari/' + common_genes_list[rand] + '.fna'
    car_path = 'all mouse genes/caroli/' + common_genes_list[rand] + '.fna'

    genomeList = open_file(mus_path, character_limit=char_limit)
    genome = ''.join(genomeList)  # combine each line of genome into 1 string
    genome = genome.replace('\n', '')  # remove newline characters

    otherGenomeList = open_file(pah_path, character_limit=char_limit)
    otherGenome = ''.join(otherGenomeList)
    otherGenome = otherGenome.replace('\n', '')  # remove newline characters

    anotherGenomeList = open_file(car_path, character_limit=char_limit)
    anotherGenome = ''.join(anotherGenomeList)
    anotherGenome = anotherGenome.replace('\n', '')

    new_genome = hide_random_sequence(genome)
    correct_values = missing_values_array(genome, new_genome)

    kn = KNearestLevenshtein()
    kn.fit(new_genome)
    preds = kn.predict([otherGenome, anotherGenome])

    amount_time = time.time() - start_time

    print('\nPRED DETAILS FOR: ' + common_genes_list[rand])
    print('time: %s' % amount_time)

    times.append(amount_time)
    acc_rates.append(calcAccuracy(correct_values, preds))
    i+=1

genes_tested = []
for j in idx:
    genes_tested.append(common_genes_list[j])
#print('Genes tested: ', genes_tested)
print('\nAVERAGE ACCURACY: ', np.mean(acc_rates))
total_time_in_seconds = np.sum(times)
total_minutes = int(total_time_in_seconds / 60)
leftover_seconds = int(total_time_in_seconds % 60)
print(f'TOTAL TIME: {total_minutes}m, {leftover_seconds}s')
