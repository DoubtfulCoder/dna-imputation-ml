import numpy as np
from species import open_file

lengths = []

common_genes = open('genes_in_all.txt', 'r')
data = common_genes.read()
common_genes_list = data.split('\n')

for i in range(3000, 6000):
    car_path = 'all mouse genes/caroli/' + common_genes_list[i] + '.fna'
    genomeList = open_file(car_path, character_limit=2000000)
    genome = ''.join(genomeList)  # combine each line of genome into 1 string
    genome = genome.replace('\n', '')  # remove newline characters

    i = 0
    while(i < len(genome)):
        if genome[i] == 'N' or genome[i] == 'n':
            blank_len = 0
            for j in range(i, len(genome)):
                if genome[j] == 'N' or genome[j] == 'n':
                    blank_len += 1
                else:
                    break
            lengths.append(blank_len)
            i += blank_len
        i += 1

print('Number of blanks: ', len(lengths))
print('Average blank space: ', np.mean(lengths))
