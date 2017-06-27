import argparse
import collections
import pandas as pd
import itertools

def haplotype_table_convert(file):
	haplotype_table = pd.read_csv(file, header=[0, 1], index_col=0, skipinitialspace=True) # remove white spaces
	haplotype_table.rename(columns=lambda x:x.strip()) # remove white spaces
	headers = list(haplotype_table.columns.values)
	
	for hap in headers:
		ref = haplotype_table.loc['*1', hap]
		haplotype_table[hap].fillna(ref, inplace=True)

	all_pairs_star_alleles = list(itertools.combinations_with_replacement(list(haplotype_table.index.astype(str)), 2))
	format_pair_names = [str(pair[0]) +'/' + str(pair[1]) for pair in all_pairs_star_alleles]
	new_diplo_dataframe = pd.DataFrame(index=format_pair_names, columns=headers, dtype=str)
	
	for pairs in all_pairs_star_alleles:
		index = str(pairs[0]) +'/' + str(pairs[1])
		temp = haplotype_table.loc[[str(pairs[0]), str(pairs[1])],]
	
		for name in headers:
			new_diplo_dataframe.set_value(index, name, temp[name].str.cat(sep='/'))


	new_diplo_dataframe.to_csv(str(file.split('.')[0])+'_converted_diplotype.csv')
	
	return str(file.split('.')[0])+'_converted_diplotype.csv'

def diplotype_translation_table(file):
	
	diplotype_table = pd.read_csv(file, header=0, index_col=0)
	headers = list(diplotype_table)

	diplo_dict = {} # example entry {*1/*1:[(g.11017a, RS933569, A/A),etc... for all rsIDs] }
	for index, row in diplotype_table.iterrows():
		diplo_dict[index] = [(str(ids).strip(), str(row[ids]).strip()) for ids in headers]

	return diplo_dict


def genotype_data(file):
	all_samples = {}
	with open(file) as sample_pheno:
		header = next(sample_pheno)
		for line in sample_pheno:
			pheno, sample, hg19, rsid = line.rstrip('\n').split(',')
			if sample in all_samples:
				all_samples[sample].extend([(str((str(hg19).strip(), str(rsid).strip())), str(pheno).strip())])
			else:
				all_samples[sample] = [(str((str(hg19).strip(), str(rsid).strip())), str(pheno).strip())]

	return all_samples


def check_genotype(diplotable, sample_calls, interpretation):
	output = open('samples_matched_with_diplotypes.tsv', 'w')
	output.write('sampleID' +'\t' + 'star_diplotype' +'\t' + 'interpretation' + '\t' + 'genotype' + '\n')
	diplotype_interpretation = {}

	with open(interpretation) as file:
		header = next(file)
		for line in file:
			line = line.strip().split(',')
			diplotype_interpretation[str(line[0])] = line[1:]

	
	for key1,value1 in sample_calls.iteritems():
		for key2,value2 in diplotable.iteritems():
			if cmp(value1, value2) == 0:
				output.write(str(key1) + '\t' +str(key2) + '\t' + str(diplotype_interpretation[key2]) + '\n')


if __name__ == '__main__':
	#parser = argparse.ArgumentParser(description = "Parse file names and data types from command line")
	#parser.add_argument('haplo_file', dest='haplo_file', type=str, help='CSV ')
	#parser.add_argument('diplo_file', dest='diplo_file', type=str, help='CSV')
	#parser.add_argument('samples', dest='samples', type=str, help='CSV')
	#parser.add_argument('diplotype_interpretation', dest='diplotype_interpretation', type=str, help='CSV')
	#args = parser.parse_args()


	hap_table_file = '/home/tonya/github_repositories/genoFinder/example_data/CYP2C19_allele_definition_table.csv'
	genotype_data_path = '/home/tonya/github_repositories/genoFinder/example_data/CYP2C19_allele_definition_table_converted_diplotype_example_sample_sheet.csv'
	diplotype_interpretation = '/home/tonya/github_repositories/genoFinder/example_data/CYP2C19_Diplotype_Phenotype_Table.csv'
	converted_table = haplotype_table_convert(file=hap_table_file)
	diplo_dict = diplotype_translation_table(file=converted_table)
	sample_calls = genotype_data(file=genotype_data_path)
	check_genotype(diplotable=diplo_dict, sample_calls=sample_calls, interpretation=diplotype_interpretation)
