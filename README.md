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
<p align="center">
<img src="https://github.com/tbrunetti/genoFinder/blob/master/diplo_file_example_annotated.png" width="700"/>
</p>


