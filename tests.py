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
char_limit = 10000

genomeList = open_file('chrI_celegans.fna', character_limit=char_limit)
genome = ''.join(genomeList)  # combine each line of genome into 1 string
genome = genome.replace('\n', '')  # remove newline characters


def testWithTwoSpecies():
    otherGenomeList = open_file(
        'chrI_cbriggsae.fna', character_limit=char_limit)
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
testWithTwoSpecies()
