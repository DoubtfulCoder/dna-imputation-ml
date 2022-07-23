### How to download the gene data

1. Create a folder called _all mouse genes_. Inside of it, create two subfolders, _musculus_ and _pahari_
2. Go to https://www.ncbi.nlm.nih.gov/labs/data-hub/gene/table/taxon/10090/ for the Mus musculus genes and https://www.ncbi.nlm.nih.gov/labs/data-hub/gene/table/taxon/10093/ for the Mus pahari genes. For each, select "Protein-coding" for Gene types. Next, click Download -> Download Package. Make sure "Gene sequences (FASTA)" is selected and download each.
3. Once each set of genes has downloaded, locate the _gene.fna_ file in each folder. Copy the path to the file and past the path for each one into _gene_open.fna_
4. Uncomment the pahari and musculus lines in which open_genes is called and run the script.
