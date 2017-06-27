# genoFinder
Algorithm to find match haplo- and diplo- star alleles to each sample haplo- and diplo- types on a per gene basis

## Arguments and Input File Formats
------------------------------------
There are **3 required arguments/files** in order to run this algorithm.  The user needs to either provide a haplotype file using the -haplo_file argument or a diplotype file using the -diplo_file argument.  Additionally a sample sheet and an interpretation table.  Please refer to the images below for more information on formatting.

| Argumment | Description |
| --- | --- |
| -haplo_file | This is a CSV file similar to the pharmGKB allele definition table.  The 1st line contains hg19 coordianates of the SNP and the 2nd line is the rsID |
| -diplo_file | This is a CSV file where the first line is a tuple of the hg19 genome coordinates following by the rsID. |
| -samples | This is a CSV file that requires 4 headers in order: Call, Sample, hg19, rsid |
| -diplotype_interpretation | A CSV file that contains the diplotype translations |

Example images of each:  
Below is an image of an example haplo_file input.  This is a slightly modified form of the pharmGKB allele definitions files for each gene.  If this file is supplied then a diplo_file is not necessary as one will be properly generated.
<p align="center">
<img src="https://github.com/tbrunetti/genoFinder/blob/master/haplo_file_example_annotated.png"/>
</p>  


Below is an image of an example diplo_file input.  This can be generated in the algorithm if a haplotable file is given using the -haplo_file argument.  This should contain every pairwise combination of star alleles.
<p align="center">
<img src="https://github.com/tbrunetti/genoFinder/blob/master/diplo_file_example_annotated.png"/>
</p>


Below is an example image of the sample sheet.  This is generated per gene and can include infinite number of patients as long as all the patients are being typed for the sample gene.  Each line is one SNP for one patient.
<p align="center">
<img src="https://github.com/tbrunetti/genoFinder/blob/master/sample_sheet_example_annotated.png"/>
</p>

Below is an example image of the interpretation table required.  This can be downloaded from pharmGKB for each gene.  It will contain every pairwise combination of star alleles and how it should be interpreted.
<p align="center">
<img src="https://github.com/tbrunetti/genoFinder/blob/master/diplotype_interpretation_example_annotated.png"/>
</p>

##  Output Files
-----------------
The output of this algorithm should be a table where each patients' diplotype for the gene of interest can be matched to a star diplotype and then interpreted.  Additionally, the full genotype of the individual should also be written out in the table.
