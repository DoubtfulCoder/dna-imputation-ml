### How to download the gene data

1. Create a folder called _all mouse genes_. Inside of it, create two subfolders, _musculus_ and _pahari_
2. Go to https://www.ncbi.nlm.nih.gov/labs/data-hub/gene/table/taxon/10090/ for the Mus musculus genes and https://www.ncbi.nlm.nih.gov/labs/data-hub/gene/table/taxon/10093/ for the Mus pahari genes. For each, select "Protein-coding" for Gene types. Next, click Download -> Download Package. Make sure "Gene sequences (FASTA)" is selected and download each.
3. Once each set of genes has downloaded, locate the _gene.fna_ file in each folder. Copy the path to the file and past the path for each one into _gene_open.fna_
4. Uncomment the pahari and musculus lines in which open_genes is called and run the script.


```bash
├── all_gene_names.txt
├── all_mus_acc.log
├── area_under_curve.py: file for calculating area under curve of maximum blank length vs. 
├── gene_logs
│   ├── skipping_plus_equal_weights_for_ins_and_del.log
│   ├── without_skipping.log
│   └── with_skipping.log
├── gene_open.py: opens a genomic FASTA file
├── genes_in_all.txt
├── genes_in_both.txt
├── knn_levenshtein.py: main algorithm file for KNN and levenshtein distance
├── message.log
├── missing_lengths.py
├── more tests
│   ├── 3_skipping_randomspecies.log
│   ├── 3_species_score_cutoff.log
│   ├── 3_species_with_skipping.log
│   ├── 3_vs_2_species.log
│   ├── 3_vs_2_species_with_skipping.log
│   ├── higher blanks spaces.log
│   ├── len_30_blanks.log
│   ├── more tests.log
│   └── mus_genes.log
├── mus_gene_tests.py
├── mus_musculus_pahari
│   ├── accuracies_maxdist.txt
│   ├── accuracies.txt
│   ├── musculus
│   │   ├── atf4.fna
│   │   ├── casd1.fna
│   │   ├── cplx3.fna
│   │   ├── egln1.fna
│   │   ├── fbxw8.fna
│   │   ├── gad2.fna
│   │   ├── lrp1b.fna
│   │   ├── mafa.fna
│   │   ├── mecp2.fna
│   │   ├── nfkb1.fna
│   │   ├── pon1.fna
│   │   ├── prkrip1.fna
│   │   ├── qdpr.fna
│   │   ├── tmem185a.fna
│   │   ├── ucp2.fna
│   │   └── zfp746.fna
│   ├── pahari
│   │   ├── atf4.fna
│   │   ├── casd1.fna
│   │   ├── cplx3.fna
│   │   ├── egln1.fna
│   │   ├── fbxw8.fna
│   │   ├── gad2.fna
│   │   ├── mafa.fna
│   │   ├── mecp2.fna
│   │   ├── nfkb1.fna
│   │   ├── pon1.fna
│   │   ├── prkrip1.fna
│   │   ├── qdpr.fna
│   │   ├── tmem185a.fna
│   │   ├── ucp2.fna
│   │   └── znf746.fna
│   ├── tests
│   │   ├── atf4.log
│   │   ├── casd1.log
│   │   ├── cplx3.log
│   │   ├── egln1.log
│   │   ├── fbxw8.log
│   │   ├── gad2.log
│   │   ├── mafa.log
│   │   ├── mecp2.log
│   │   ├── nfkb1.log
│   │   ├── pon1.log
│   │   ├── prkrip1.log
│   │   ├── qdpr.log
│   │   ├── tmem185a.log
│   │   ├── ucp2.log
│   │   └── znf746.log
│   └── tests_maxdist
│       ├── atf4.log
│       ├── casd1.log
│       ├── cplx3.log
│       ├── egln1.log
│       ├── fbxw8.log
│       ├── gad2.log
│       ├── mafa.log
│       ├── mecp2.log
│       ├── nfkb1.log
│       ├── pon1.log
│       ├── prkrip1.log
│       ├── qdpr.log
│       ├── tmem185a.log
│       ├── ucp2.log
│       └── znf746.log
├── score_cutoff_tests.py
├── species.py
├── tests_blank_len_for_graph.log
├── tests_for_area.log
├── tests.py
└── tests_with_mis18bp1.log
```
