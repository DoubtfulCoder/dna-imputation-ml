import random
import numpy as np


# Opens chromosome file
def open_file(file_name, character_limit=3000):
    with open(file_name, 'r') as f:
        return f.readlines(character_limit)[1:]


# Hides random sequences of bases in the genome
def hide_random_sequence(genome, max_length=6):
    iters = int(len(genome) / 70)  # number of times we should hide a sequence
    for i in range(iters):
        # hide sequences of random length from 1 to max_length
        hidden_sequence_length = random.randint(1, max_length)
        # pick a random position and hide sequence starting from there
        start_index = random.randint(0, len(genome) - hidden_sequence_length)
        new_genome = genome[:start_index]
        # add blank spaces for hidden part
        for j in range(hidden_sequence_length):
            new_genome += ' '
        # add in everything else
        new_genome += genome[start_index + hidden_sequence_length:]
        genome = new_genome
    return genome


def missing_values_array(genome, new_genome):
    correct_values = []
    i = 0
    while(i < len(new_genome)):
        if new_genome[i] == ' ':
            blank_len = 0
            for j in range(i, len(new_genome)):
                if new_genome[j] == ' ':
                    blank_len += 1
                else:
                    break
            correct_values.append(genome[i:i+blank_len])
            i += blank_len
        i += 1
    return correct_values


class KNearestLevenshtein:
    def __init__(self, s_range=1000, area=10, max_ld=3, k=5):
        # defines how far back and forward the model will look from the location of the missing values for imputation
        self.search_range = s_range

        # defines how far back and forward will the model take a substring from the blank spaces to calculate the levenshtein distance
        self.search_area = area

        # defines the maximum levenshtein distance which is acceptable for imputation
        self.levDist_max = max_ld

        # defines how many neighbors the program will consider
        self.k_neighbors = k

    # the function that will return a 2D array having levenshtein distances between respective indices of string 1 and 2.
    def levenshteinDistanceCalc(token1, token2):
        distances = np.zeros((len(token1) + 1, len(token2) + 1))

        for t1 in range(len(token1) + 1):
            distances[t1][0] = t1

        for t2 in range(len(token2) + 1):
            distances[0][t2] = t2

        a = 0
        b = 0
        c = 0

        for t1 in range(1, len(token1) + 1):
            for t2 in range(1, len(token2) + 1):
                if (token1[t1-1] == token2[t2-1]):
                    distances[t1][t2] = distances[t1 - 1][t2 - 1]
                else:
                    a = distances[t1][t2 - 1]
                    b = distances[t1 - 1][t2]
                    c = distances[t1 - 1][t2 - 1]

                    if (a <= b and a <= c):
                        distances[t1][t2] = a + 1
                    elif (b <= a and b <= c):
                        distances[t1][t2] = b + 1
                    else:
                        distances[t1][t2] = c + 1

        # return the levenshtein distance
        return distances[len(token1)][len(token2)]

    # Fits model to a sequence in genome with next 4 characters to be predicted
    def fit(self, species):
        # later to be changed into a for loop in order to account for multiple species
        self.species = species

    # Predicts/imputes next four characters based on another species
    def predict(self, other_species):
        i = 0
        actual_preds = []
        while(i < len(self.species)):
            if self.species[i] == ' ':
                blank_len = 0
                blank_idx = i
                for j in range(i, len(self.species)):
                    if self.species[j] == ' ':
                        blank_len += 1
                    else:
                        break
                neighbors = KNearestLevenshtein.get_neighbors(
                    self, self.species, other_species, blank_len, blank_idx)
                # print('neighbors for blank space at ', i, 'are: ', neighbors)

                # Make dictionary of predictions and # of times they appear
                predictions = {}
                for neighbor in neighbors:
                    if neighbor[0] in predictions:
                        predictions[neighbor[0]] += 1
                    else:
                        predictions[neighbor[0]] = 1
                #print('preds', predictions)

                # Find most common prediction
                max_prediction = max(predictions, key=predictions.get)
                actual_preds.append(max_prediction)
                i += blank_len
            i += 1
        return actual_preds

    # Gets the k most similar neighbors using levenshtein distance
    def get_neighbors(self, correct_seq, other_species, blank_len, blank_idx):
        neighbors = []

        # Loop over other species genome 4 characters at a time
        for i in range(0, len(other_species) - self.search_area - blank_len):
            # Check every substring of 20 chars in other_species
            substring_pre = other_species[i:i + self.search_area]
            substring_post = other_species[i + self.search_area +
                                           blank_len:i + 2*(self.search_area)+blank_len]
            prediction = other_species[i + self.search_area +
                                       1:i + self.search_area + 1 + blank_len]
            neighbors.append((prediction, (KNearestLevenshtein.levenshteinDistanceCalc(substring_pre, correct_seq[blank_idx - self.search_area - 1: blank_idx]) + KNearestLevenshtein.levenshteinDistanceCalc(
                substring_pre, correct_seq[blank_idx + blank_len: blank_idx + blank_len + self.search_area]))/2))

        # Sort neighbors by distance
        neighbors.sort(key=lambda tup: tup[1])
        return neighbors[:self.k_neighbors]


# file opening and base hiding tests
genomeList = open_file('chrI_celegans.fna')
genome = ''.join(genomeList)  # combine each line of genome into 1 string
genome = genome.replace('\n', '')  # remove newline characters
otherGenomeList = open_file('chrI_cbriggsae.fna')
# combine each line of genome into 1 string
otherGenome = ''.join(otherGenomeList)
otherGenome = otherGenome.replace('\n', ' ')  # remove newline characters
new_genome = hide_random_sequence(genome)
correct_values = missing_values_array(genome, new_genome)
# print(otherGenome, '\n')
# print(new_genome, '\n')
# print(correct_values)

# predicting
kn = KNearestLevenshtein()
kn.fit(new_genome)
preds = kn.predict(otherGenome)

# print(correct_values, '\n')
# print(preds)

num_correct = 0
num_total = 0
for i in range(len(correct_values)):
    correct = correct_values[i]
    pred = preds[i]
    for j in range(len(correct)):
        if correct[j] == pred[j]:
            num_correct += 1
        num_total += 1
print('Accuracy: ', num_correct/num_total)

# tests
# print(KNearestLevenshtein.levenshteinDistanceCalc("hello", "hello"))
# print(KNearestLevenshtein.levenshteinDistanceCalc("hello", "helloo"))
# print(KNearestLevenshtein.levenshteinDistanceCalc("hello", "houswo"))

# train = "GATCTTTTCTATTCCCTAAC    GTTTCGAACAGCGCGGTTCCCCAGTAGCGAAAAT  CACAAACAAATAGTAGCAAAAT"
# test = "CAGATTCGGAAAAGGGATATTAAGGCGAATTTGAATGGTCCAGTAGTGAAAATATCACAAACAAAAAGTAGAAAAATGTGATCTTTTCTATTCCCTAAAAAGCGTTTCGAAAAGCGCGGTTCCGTGTGGATTTCCCAATTTTGGAAGTTAATGGACCAAAATCGCGCAAAAAACACGGGCACACCTGATGAATCAGTTTTGCAAAATCCTGCAAAAAATATTTCAACGTACTCACGTTAACTCATTCAGGAAATCAATGAGATCAATGTGTACGATAGGTTTGTGCCCGTGACAAAGGATCAGCAATTTTCAGAAGAGGCGCCAGAAAATTTGTGTTTTTGAATTTGCGCAATACAATTTTCAATCCACACAGACTTTTTTTGTATTATTTTCAATCCAA"

#print(KNearestLevenshtein.get_neighbors(train, test, 5))

# tests with oop
# kn = KNearestLevenshtein()
# kn.fit(train)
# kn.predict(test)
