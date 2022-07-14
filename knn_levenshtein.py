import numpy as np

class KNearestLevenshtein
{
    def __init__():
        #defines how far back and forward the model will look from the location of the missing values for imputation
        search_Range = 1000

        #defines how far back and forward will the model take a substring from the blank spaces to calculate the levenshtein distance
        search_Area = 10 

        #defines the maximum levenshtein distance which is acceptable for imputation
        levDist_max = 2

    #the function that will return a 2D array having levenshtein distances between respective indices of string 1 and 2. 
    def levenshteinDistanceCalc(token1, token2):
        distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

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
    
        return distances

    def fit():

    def predict():
}