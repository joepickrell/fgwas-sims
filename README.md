## Simulations of performance of fgwas ##

These directories contain the data and code I used to test the performance of fgwas. Scripts are customized to the cluster I use and will thus need to be modified to run on machines other than mine.


### Requirements ###
[hapgen2](https://mathgen.stats.ox.ac.uk/genetics_software/hapgen/hapgen2.html)

[fgwas](https://github.com/joepickrell/fgwas)

### Description ###
Simulations are based on the haplotype structure of 111 random regions (2 per chromosome, plus an extra chromosome 22 region) from real 1000 Genomes data. Each simulation consists of simulated genotype and phenotype data for 5,000 individuals at all 111 regions. To run the simulations, go to sims/scripts/. The steps are listed in order in that directory (i.e. first run the script 1_*, then the script 2_*, then 3_*, etc.:

1. Simulate 10,000 control haplotypes using hapgen2
2. Simulate quantiative phenotypes for 5,000 individuals using the haplotypes from 1 (~50% of the variance explained by the 111 causal SNPs in subset/causals.txt)
3. Perform association testing for each SNP
4. Convert the output to fgwas format
5. Simulate annotations (need to supply the rate at which causal SNPs fall in the annotation and the rate at which non-causal SNPs fall in the annotation)
6. Run fgwas

