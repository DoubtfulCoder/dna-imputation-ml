import time

import numpy as np

from knn_levenshtein import KNearestLevenshtein
from species import hide_random_sequence, missing_values_array, open_file

# train = "GATCTTTTCTATTCCCTAAC    GTTTCGAACAGCGCGGTTCCCCAGTAGCGAAAAT  CACAAACAAATAGTAGCAAAAT"
# test = "CAGATTCGGAAAAGGGATATTAAGGCGAATTTGAATGGTCCAGTAGTGAAAATATCACAAACAAAAAGTAGAAAAATGTGATCTTTTCTATTCCCTAAAAAGCGTTTCGAAAAGCGCGGTTCCGTGTGGATTTCCCAATTTTGGAAGTTAATGGACCAAAATCGCGCAAAAAACACGGGCACACCTGATGAATCAGTTTTGCAAAATCCTGCAAAAAATATTTCAACGTACTCACGTTAACTCATTCAGGAAATCAATGAGATCAATGTGTACGATAGGTTTGTGCCCGTGACAAAGGATCAGCAATTTTCAGAAGAGGCGCCAGAAAATTTGTGTTTTTGAATTTGCGCAATACAATTTTCAATCCACACAGACTTTTTTTGTATTATTTTCAATCCAA"

#print(KNearestLevenshtein.get_neighbors(train, test, 5))

# tests with oop
# kn = KNearestLevenshtein()
# kn.fit(train)
# kn.predict(test)

# file opening and base hiding tests

path1 = 'mus_musculus_pahari/musculus/zfp746.fna'
path2 = 'mus_musculus_pahari/pahari/znf746.fna'

path3 = 'mus_musculus_pahari/musculus/nfkb1.fna'
path4 = 'mus_musculus_pahari/pahari/nfkb1.fna'

path5 = 'mus_musculus_pahari/musculus/prkrip1.fna'
path6 = 'mus_musculus_pahari/pahari/prkrip1.fna'

path7 = 'mus_musculus_pahari/musculus/mecp2.fna'
path8 = 'mus_musculus_pahari/pahari/mecp2.fna'

path9 = 'mus_musculus_pahari/musculus/mafa.fna'
path10 = 'mus_musculus_pahari/pahari/mafa.fna'

path11 = 'mus_musculus_pahari/musculus/tmem185a.fna'
path12 = 'mus_musculus_pahari/pahari/tmem185a.fna'

path13 = 'mus_musculus_pahari/musculus/casd1.fna'
path14 = 'mus_musculus_pahari/pahari/casd1.fna'

path15 = 'mus_musculus_pahari/musculus/pon1.fna'
path16 = 'mus_musculus_pahari/pahari/pon1.fna'

path17 = 'mus_musculus_pahari/musculus/gad2.fna'
path18 = 'mus_musculus_pahari/pahari/gad2.fna'

path19 = 'mus_musculus_pahari/musculus/ucp2.fna'
path20 = 'mus_musculus_pahari/pahari/ucp2.fna'

path21 = 'mus_musculus_pahari/musculus/atf4.fna'
path22 = 'mus_musculus_pahari/pahari/atf4.fna'

path23 = 'mus_musculus_pahari/musculus/egln1.fna'
path24 = 'mus_musculus_pahari/pahari/egln1.fna'

path25 = 'mus_musculus_pahari/musculus/qdpr.fna'
path26 = 'mus_musculus_pahari/pahari/qdpr.fna'

path27 = 'mus_musculus_pahari/musculus/cplx3.fna'
path28 = 'mus_musculus_pahari/pahari/cplx3.fna'

path29 = 'mus_musculus_pahari/musculus/fbxw8.fna'
path30 = 'mus_musculus_pahari/pahari/fbxw8.fna'

char_limit = 100000

# genomeList = open_file('chrI_celegans.fna', character_limit=char_limit)
genomeList = open_file(path15, character_limit=char_limit)
genome = ''.join(genomeList)  # combine each line of genome into 1 string
genome = genome.replace('\n', '')  # remove newline characters


def testWithTwoSpecies():
    # otherGenomeList = open_file(
    #     'chrI_cbriggsae.fna', character_limit=char_limit)
    otherGenomeList = open_file(path16, character_limit=char_limit)
    # combine each line of genome into 1 string
    otherGenome = ''.join(otherGenomeList)
    otherGenome = otherGenome.replace('\n', '')  # remove newline characters

    new_genome = hide_random_sequence(genome)
    correct_values = missing_values_array(genome, new_genome)

    print('length 1:', len(genome))
    print('length 2:', len(otherGenome))

    kn = KNearestLevenshtein()
    kn.fit(new_genome)
    preds = kn.predict(otherGenome)

    print('correct values:', correct_values, '\n')
    print('predictions:', preds)
    calcAccuracy(correct_values, preds)


def testWithOneSpecies():
    genomeList = open_file('chrI_celegans.fna', character_limit=2*char_limit)
    genome = ''.join(genomeList)  # combine each line of genome into 1 string
    genome = genome.replace('\n', '')  # remove newline characters

    genome_missing = genome[:int(len(genome)/2)]
    genome_full = genome[int(len(genome)/2):]

    new_genome = hide_random_sequence(genome_missing)
    correct_values = missing_values_array(genome_missing, new_genome)

    print(len(new_genome))
    print(len(genome_full))

    kn = KNearestLevenshtein()
    kn.fit(new_genome)
    preds = kn.predict(genome_full)

    print('correct values:', correct_values, '\n')
    print('predictions:', preds)
    calcAccuracy(correct_values, preds)


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


# testWithOneSpecies()
start_time = time.time()
testWithTwoSpecies()
print('time: %s' % (time.time() - start_time))
