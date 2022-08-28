### How to download the gene data

1. Create a folder called _all mouse genes_. Inside of it, create two subfolders, _musculus_ and _pahari_
2. Go to https://www.ncbi.nlm.nih.gov/labs/data-hub/gene/table/taxon/10090/ for the Mus musculus genes and https://www.ncbi.nlm.nih.gov/labs/data-hub/gene/table/taxon/10093/ for the Mus pahari genes. For each, select "Protein-coding" for Gene types. Next, click Download -> Download Package. Make sure "Gene sequences (FASTA)" is selected and download each.
3. Once each set of genes has downloaded, locate the _gene.fna_ file in each folder. Copy the path to the file and past the path for each one into _gene_open.fna_
4. Uncomment the pahari and musculus lines in which open_genes is called and run the script.


```bash
├── knn_levenshtein.py: main algorithm file for KNN and levenshtein distance
├── gene_open.py: converts FASTA file for Mus genus into individual gene files (make sure to change paths)
├── species.py: contains common species methods like imputing values
├── mus_gene_tests.py: use this file for running tests
├── tests.py: old file that had tests for just a few genes
├── area_under_curve.py: file for calculating area under curve of maximum blank length vs. accuracy
├── score_cutoff_tests.py: a file for time tests for different score cutoffs and strings
├── missing_lengths.py: file for calculating average missing blank space in real world data
├── gene_logs
│   ├── skipping_plus_equal_weights_for_ins_and_del.log: details of tests run with no weight modification to levenshtein distance
│   ├── without_skipping.log: details of tests run without implementation of a method that skips iterations
│   └── with_skipping.log: details of tests run run with the method that skips iterations when a certain condition is met
├── more tests
│   ├── 3_skipping_randomspecies.log: details of tests run on randomly selected genes with two species(caroli and pahari) for imputation with skipping
│   ├── 3_species_score_cutoff.log: details of tests run with two species(caroli and pahari) for imputation with a score cutoff
│   ├── 3_species_with_skipping.log: details of tests run with 5 representative genes from two species(caroli and pahari) for imputation with skipping
│   ├── 3_vs_2_species.log: comparison of accuracy of the algorithm with one species  vs two for imputation of 5 representative genes
│   ├── 3_vs_2_species_with_skipping.log: comparison of accuracy of the algorithm with one species  vs two for imputation of 5 representative genes with skipping
│   ├── higher blanks spaces.log: multiple tests run on 5 representative genes with a different maximum blank space length each time
│   ├── len_30_blanks.log
│   ├── more tests.log: tests run on a high number of randomly selected genes to test if algorithm works well for all genes
│   └── mus_genes.log
├── mus_musculus_pahari
│   ├── accuracies_maxdist.txt
│   ├── accuracies.txt
│   ├── musculus
│   ├── pahari
│   ├── tests
│   └── tests_maxdist
├── all_mus_acc.log
├── message.log
├── tests_blank_len_for_graph.log
├── tests_for_area.log: multiple tests run on 5 representative genes with different values of search area each time
├── tests_with_mis18bp1.log
├── genes_in_both.txt: list of genes common in mus musculus and pahari
└── genes_in_all.txt: list of genes common in mus musculus, pahari and caroli
```
