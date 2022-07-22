import sys
from os import listdir
from os.path import isfile, join

from pyrsistent import m

log_file = open("message.log", "w")
sys.stdout = log_file

path_musculus = '/home/naveed/Downloads/mus_musculus_all_proteins/ncbi_dataset/data/gene.fna'
path_pahari = '/home/naveed/Downloads/mus_pahari_all_genes/ncbi_dataset/data/gene.fna'


def open_genes(file_name, gene_extraction_path, line_limit=20000, list_of_genes_to_use=None):
    file = open(file_name, 'r')
    gene_names = []
    genes = []
    current_gene = ''
    currently_reading_gene = True
    for i in range(line_limit):
        line = file.readline()
        if not line:  # reached end of file
            break
        # new gene lines start with '>'
        if line[0] == '>':
            line = line.split()
            gene_name = line[1]  # name of gene is second word

            # LOC genes are specific to pahari
            if gene_name.startswith('LOC'):
                print("LOC gene found: " + gene_name)
                break

            # use only genes that are specified in list_of_genes_to_use
            if list_of_genes_to_use is not None:
                # don't make files for genes that are not in list_of_genes_to_use
                if gene_name not in list_of_genes_to_use:
                    # not adding this gene so dont read data
                    currently_reading_gene = False
                    continue

            gene_names.append(gene_name)
            if current_gene != '' and currently_reading_gene:
                # add previous gene to list
                # but not for first gene since their is no previous gene
                genes.append(current_gene)
            current_gene = ''  # reset current gene since new gene started
            currently_reading_gene = True
        elif currently_reading_gene:
            current_gene += line  # still adding to current gene

    if currently_reading_gene:
        genes.append(current_gene)  # add last gene to list

    print(len(genes))
    print(len(gene_names))

    # create files for each gene
    for j in range(len(genes)):
        print(gene_names[j])
        print(genes[j])
        gene_file = open(gene_extraction_path + gene_names[j] + '.fna', 'w')
        gene_file.write(genes[j])
        gene_file.close()

    j_plus_one = j + 1
    print("rest of gene names", gene_names[j_plus_one:])
    return gene_names


musculus_gene_extraction_path = 'all mouse genes/musculus/'
pahari_gene_extraction_path = 'all mouse genes/pahari/'

# genomeList = open_genes(
#     path_pahari, pahari_gene_extraction_path, line_limit=2000000000000)

# get all the file names in pahari directory (removes the .fna extension)
# used to ensure we only get files in musculus that are in pahari
all_files_in_pahari = [f.replace('.fna', '') for f in listdir(
    pahari_gene_extraction_path) if isfile(join(pahari_gene_extraction_path, f))]

print(all_files_in_pahari)

genomeList = open_genes(
    path_musculus, musculus_gene_extraction_path,
    line_limit=200000, list_of_genes_to_use=all_files_in_pahari)


# genome = ''.join(genomeList)  # combine each line of genome into 1 string
# genome = genome.replace('\n', '')  # remove newline characters
# print(genome)

print('num_musc_in_pahari', 15183)
print('num_pahari_in_musc', 15174)
