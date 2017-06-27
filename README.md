# genoFinder
Algorithm to find match haplo- and diplo- star alleles to each sample haplo- and diplo- types on a per gene basis

## Arguments and Input File Formats
------------------------------------
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


Below is an image of an example diplo_file input.  This can be generated in the algorithm if a haplotable file is given using the -haplo_file argument.
<p align="center">
<img src="https://github.com/tbrunetti/genoFinder/blob/master/diplo_file_example_annotated.png"/>
</p>


Below is an example image of the sample sheet.  This is generated per gene and can include infinite number of patients as long as all the patients are being typed for the sample gene.  Each line is one SNP for one patient.
<p align="center">
<img src="https://github.com/tbrunetti/genoFinder/blob/master/sample_sheet_example_annotated.png"/>
</p>

