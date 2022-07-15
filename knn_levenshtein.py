import numpy as np


class KNearestLevenshtein:
    def __init__(self, s_range=1000, area=10, max=3):
        # defines how far back and forward the model will look from the location of the missing values for imputation
        self.search_range = s_range

        # defines how far back and forward will the model take a substring from the blank spaces to calculate the levenshtein distance
        self.search_area = area

        # defines the maximum levenshtein distance which is acceptable for imputation
        self.levDist_max = max

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

    # Fits model to a sequence in genome with next 4 characters to be predicted
    def fit(self, species):
        self.species = species

    # Predicts/imputes next four characters based on another species
    def predict(self, other_species):
        neighbors = KNearestLevenshtein.get_neighbors(
            self.species, other_species, 4)
        print('neighbors', neighbors)

        # Make dictionary of predictions and # of times they appear
        predictions = {}
        for neighbor in neighbors:
            if neighbor[1] in predictions:
                predictions[neighbor[1]] += 1
            else:
                predictions[neighbor[1]] = 1
        print('preds', predictions)

        # Find most common prediction
        max_prediction = max(predictions, key=predictions.get)
        print('max prediction', max_prediction)

        return max_prediction

    # Gets the k most similar neighbors using levenshtein distance
    def get_neighbors(correct_seq, other_species, k):
        neighbors = []

        # Loop over other species genome 4 characters at a time
        for i in range(0, len(other_species)-24, 4):
            # Check every substring of 20 chars in other_species
            substring = other_species[i:i+20]
            prediction = other_species[i+20:i+24]
            neighbors.append((substring, prediction,
                              KNearestLevenshtein.levenshteinDistanceCalc(substring, correct_seq)))

        # Sort neighbors by distance
        neighbors.sort(key=lambda tup: tup[2])

        return neighbors[:k]


# tests
print(KNearestLevenshtein.levenshteinDistanceCalc("hello", "hello"))
print(KNearestLevenshtein.levenshteinDistanceCalc("hello", "helloo"))
print(KNearestLevenshtein.levenshteinDistanceCalc("hello", "houswo"))

train = "CACAGACTTTTCTGGATATG"
test = "CAGATTCGGAAAAGGGATATTAAGGCGAATTTGAATGGTCCAGTAGTGAAAATATCACAAACAAAAAGTAGAAAAATGTGATCTTTTCTATTCCCTAAAAAGCGTTTCGAAAAGCGCGGTTCCGTGTGGATTTCCCAATTTTGGAAGTTAATGGACCAAAATCGCGCAAAAAACACGGGCACACCTGATGAATCAGTTTTGCAAAATCCTGCAAAAAATATTTCAACGTACTCACGTTAACTCATTCAGGAAATCAATGAGATCAATGTGTACGATAGGTTTGTGCCCGTGACAAAGGATCAGCAATTTTCAGAAGAGGCGCCAGAAAATTTGTGTTTTTGAATTTGCGCAATACAATTTTCAATCCACACAGACTTTTTTTGTATTATTTTCAATCCAA"

print(KNearestLevenshtein.get_neighbors(train, test, 5))

# tests with oop
kn = KNearestLevenshtein()
kn.fit(train)
print(kn.predict(test))
