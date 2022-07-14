import numpy as np

class KNearestLevenshtein
{
    #defines how far back and forward the model will look from the location of the missing values for imputation
    search_Range = 100000 

    #defines the maximum levenshtein distance which is acceptable for imputation
    levDist_max = 3

    #the function that will return a 2D array having levenshtein distances between respective indices of string 1 and 2. 
    def levenshteinDistanceCalc(token1, token2):
        distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

        for t1 in range(len(token1) + 1):
            distances[t1][0] = t1

        for t2 in range(len(token2) + 1):
            distances[0][t2] = t2

        return distances

    def fit():

    def predict():
}