import time

from Levenshtein import distance

start = time.time()
for i in range(1000000):
    distance("CGATTACGAGATCGATCGATCAGTCAGCTA", "CAGTCGATTATTCTAGCATGCTAG", weights = (2,2,1))
    distance("wiuefhw7e832y87r wefiuhw ",
             "98eegoirgj 12 asacasncjakn", weights = (2,2,1))
    distance("sbvjhdgvbysuhwiefhn",
             "fheruighispawefoiwehjfuweiefwheifwe", weights = (2,2,1))
    distance("wiowhefw2389ru23hiwuf wenbg32r1uy3rj 12nr13ruiwefv, mse.fveslirkgves,nkvber gv rfwejfw",
             "928764rt2v 32r23rj23hbrh wsacsdcsrflwoieufhv wefsdvdsnuyvq bnqwerre qre w", weights = (2,2,1))
print(time.time() - start)

start = time.time()
for i in range(1000000):
    distance("CGATTACGAGATCGATCGATCAGTCAGCTA",
             "CAGTCGATTATTCTAGCATGCTAG",weights = (2,2,1), score_cutoff=1)
    distance("wiuefhw7e832y87r wefiuhw ",
             "98eegoirgj 12 asacasncjakn",weights = (2,2,1), score_cutoff=1)
    distance("sbvjhdgvbysuhwiefhn",
             "fheruighispawefoiwehjfuweiefwheifwe",weights = (2,2,1), score_cutoff=1)
    distance("wiowhefw2389ru23hiwuf wenbg32r1uy3rj 12nr13ruiwefv, mse.fveslirkgves,nkvber gv rfwejfw",
             "928764rt2v 32r23rj23hbrh wsacsdcsrflwoieufhv wefsdvdsnuyvq bnqwerre qre w",weights = (2,2,1), score_cutoff=1)
print(time.time() - start)


start = time.time()
for i in range(1000000):
    distance("CGATTACGAGATCGATCGATCAGTCAGCTA",
             "CAGTCGATTATTCTAGCATGCTAG",weights = (2,2,1), score_cutoff=3)
    distance("wiuefhw7e832y87r wefiuhw ",
             "98eegoirgj 12 asacasncjakn",weights = (2,2,1), score_cutoff=3)
    distance("sbvjhdgvbysuhwiefhn",
             "fheruighispawefoiwehjfuweiefwheifwe",weights = (2,2,1), score_cutoff=3)
    distance("wiowhefw2389ru23hiwuf wenbg32r1uy3rj 12nr13ruiwefv, mse.fveslirkgves,nkvber gv rfwejfw",
             "928764rt2v 32r23rj23hbrh wsacsdcsrflwoieufhv wefsdvdsnuyvq bnqwerre qre w",weights = (2,2,1), score_cutoff=3)
print(time.time() - start)


start = time.time()
for i in range(1000000):
    distance("CGATTACGAGATCGATCGATCAGTCAGCTA",
             "CAGTCGATTATTCTAGCATGCTAG",weights = (2,2,1), score_cutoff=5)
    distance("wiuefhw7e832y87r wefiuhw ",
             "98eegoirgj 12 asacasncjakn",weights = (2,2,1), score_cutoff=5)
    distance("sbvjhdgvbysuhwiefhn",
             "fheruighispawefoiwehjfuweiefwheifwe",weights = (2,2,1), score_cutoff=5)
    distance("wiowhefw2389ru23hiwuf wenbg32r1uy3rj 12nr13ruiwefv, mse.fveslirkgves,nkvber gv rfwejfw",
             "928764rt2v 32r23rj23hbrh wsacsdcsrflwoieufhv wefsdvdsnuyvq bnqwerre qre w",weights = (2,2,1), score_cutoff=5)
print(time.time() - start)


start = time.time()
for i in range(1000000):
    distance("CGATTACGAGATCGATCGATCAGTCAGCTA",
             "CAGTCGATTATTCTAGCATGCTAG",weights = (2,2,1), score_cutoff=10)
    distance("wiuefhw7e832y87r wefiuhw ",
             "98eegoirgj 12 asacasncjakn",weights = (2,2,1), score_cutoff=10)
    distance("sbvjhdgvbysuhwiefhn",
             "fheruighispawefoiwehjfuweiefwheifwe",weights = (2,2,1), score_cutoff=10)
    distance("wiowhefw2389ru23hiwuf wenbg32r1uy3rj 12nr13ruiwefv, mse.fveslirkgves,nkvber gv rfwejfw",
             "928764rt2v 32r23rj23hbrh wsacsdcsrflwoieufhv wefsdvdsnuyvq bnqwerre qre w",weights = (2,2,1), score_cutoff=10)
print(time.time() - start)


start = time.time()
for i in range(1000000):
    distance("CGATTACGAGATCGATCGATCAGTCAGCTA",
             "CAGTCGATTATTCTAGCATGCTAG", weights = (2,2,1), score_cutoff=10)
    distance("wiuefhw7e832y87r wefiuhw ",
             "98eegoirgj 12 asacasncjakn",weights = (2,2,1),score_cutoff=10)
    distance("sbvjhdgvbysuhwiefhn",
             "fheruighispawefoiwehjfuweiefwheifwe",weights = (2,2,1), score_cutoff=10)
    distance("wiowhefw2389ru23hiwuf wenbg32r1uy3rj 12nr13ruiwefv, mse.fveslirkgves,nkvber gv rfwejfw",
             "928764rt2v 32r23rj23hbrh wsacsdcsrflwoieufhv wefsdvdsnuyvq bnqwerre qre w",weights = (2,2,1), score_cutoff=68)
print(time.time() - start)
