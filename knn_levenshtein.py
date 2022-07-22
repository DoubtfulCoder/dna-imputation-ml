import sys

import numpy as np
from Levenshtein import distance, hamming

# Redirect output to file for easier viewing
log_file = open("message.log", "w")
sys.stdout = log_file


class KNearestLevenshtein:
    def __init__(self, s_range=1000, area=20, max_ld=3, k=10):
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
        # return hamming(token1, token2)
        return distance(token1, token2, weights=(2, 2, 1))
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

    # Fits model to a sequence
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
                #print('neighbors for blank space at ', i, 'are: ', neighbors)

                # Make dictionary of predictions and # of times they appear
                predictions = {}
                total_levenshtein = 0
                for neighbor in neighbors:
                    total_levenshtein += neighbor[1]
                    if neighbor[0] in predictions:
                        predictions[neighbor[0]] += 1
                    else:
                        predictions[neighbor[0]] = 1
                #print('preds', predictions)
                # print(total_levenshtein / len(neighbors))
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
                                           blank_len: i + 2*(self.search_area)+blank_len]
            prediction = other_species[i +
                                       self.search_area:i + self.search_area + blank_len]
            neighbors.append((prediction, (KNearestLevenshtein.levenshteinDistanceCalc(substring_pre, correct_seq[blank_idx - self.search_area: blank_idx]) + KNearestLevenshtein.levenshteinDistanceCalc(
                substring_post, correct_seq[blank_idx + blank_len: blank_idx + blank_len + self.search_area]))/2))

        # Sort neighbors by distance
        neighbors.sort(key=lambda tup: tup[1])
        least_lev = neighbors[0][1]
        # lev_count = 0
        # for neighbor in neighbors:
        #     if neighbor[1] - least_lev <= 3:
        #         k_count += 1
        #     else:
        #         break
        # if lev_count < self.k_neighbors:
        #     return neighbors[:self.k_neighbors]
        # else:
        #     return neighbors[:lev_count]

        # adding a max dist
        k_count = 0
        for neighbor in neighbors:
            if neighbor[1] - least_lev <= 3:
                k_count += 1
            else:
                break
        number_neigbors = min(k_count, self.k_neighbors)
        return neighbors[:number_neigbors]
