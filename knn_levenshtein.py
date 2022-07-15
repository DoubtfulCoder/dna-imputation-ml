import numpy as np
import sklearn as sk
from sklearn.neighbors import KNeighborsClassifier


class KNearestLevenshtein:
    def __init__(self):
        # defines how far back and forward the model will look from the location of the missing values for imputation
        search_Range = 1000

        # defines how far back and forward will the model take a substring from the blank spaces to calculate the levenshtein distance
        search_Area = 10

        # defines the maximum levenshtein distance which is acceptable for imputation
        levDist_max = 3

    def __init__(self, s_range, area, max):
        # defines how far back and forward the model will look from the location of the missing values for imputation
        search_Range = s_range

        # defines how far back and forward will the model take a substring from the blank spaces to calculate the levenshtein distance
        search_Area = area

        # defines the maximum levenshtein distance which is acceptable for imputation
        levDist_max = max
        KNeighborsClassifier()

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

        # print(distances)
        return distances[len(token1)][len(token2)]

    def fit():
        pass

    def predict():
        pass

    # Gets the k most similar neighbors using levenshtein distance
    def get_neighbors(correct_seq, other_species, k):
        neighbors = []

        # Loop over other species genome 4 characters at a time
        for i in range(0, len(other_species)-20, 4):
            # Check every substring of 20 chars in other_species
            substring = other_species[i:i+20]
            neighbors.append((substring,
                              KNearestLevenshtein.levenshteinDistanceCalc(substring, correct_seq)))

        # Sort neighbors by distance
        neighbors.sort(key=lambda tup: tup[1])

        return neighbors[:k]


# tests
print(KNearestLevenshtein.levenshteinDistanceCalc("hello", "hello"))
print(KNearestLevenshtein.levenshteinDistanceCalc("hello", "helloo"))
print(KNearestLevenshtein.levenshteinDistanceCalc("hello", "houswo"))


# train = [
#     "GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGC",
#     "CTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCT",
#     "AAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA",
#     "GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGC",
#     "CTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCT"
# ]

train = "CAGATTCGGAAAAGGGATATTAAGGCGAATTTGAATGGTCCAGTAGTGAAAATATCACAAACAAAAAGTAGAAAAATGTGATCTTTTCTATTCCCTAAAAAGCGTTTCGAAAAGCGCGGTTCCGTGTGGATTTCCCAATTTTGGAAGTTAATGGACCAAAATCGCGCAAAAAACACGGGCACACCTGATGAATCAGTTTTGCAAAATCCTGCAAAAAATATTTCAACGTACTCACGTTAACTCATTCAGGAAATCAATGAGATCAATGTGTACGATAGGTTTGTGCCCGTGACAAAGGATCAGCAATTTTCAGAAGAGGCGCCAGAAAATTTGTGTTTTTGAATTTGCGCAATACAATTTTCAATCCACACAGACTTTTTTTGTATTATTTTCAATCCAA"

test = "CACAGACTTTTCTGGATATG"

print(KNearestLevenshtein.get_neighbors(test, train, 5))
