# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import xml_parser
import os
import visualization	#Αυτό μην το σβήνεις!
import modality
import pandas as pd
import plot_pitches as pp
import peak
import csv
import phrase
import markov_frequency_tables as mft
import math
import copy
import melismaticity
from collections import Counter
import tonoi
import numpy as np
from scipy.spatial import distance
from itertools import product

import byzmusic2staff as b2s
#import byzTree
#import markov
#import melodicContour as mc
#import voiced
#from abcd import pitch_list
#import tree
#import numpy as np
#import copy 
#import trie

#import clusterByCadence

import seaborn as sns
sns.set_theme()






all_echoi = ['echos_a', 'echos_b', 'echos_c', 'echos_d', 'echos_pla', 'echos_plb', 'echos_plc' , 'echos_pld']
all_corpus_group = ['1','2']
all_corpora = ['pro-karykis','karykis','balasis']
all_methods = ['classical_and_pitch_profile', 'triangles_similarity', 'markov_and_entropies', 'melismaticity', 'print_diagram', 'entropies_over_syllable']

CORPUS_PATH = 'corpus_uncut'



#depricated.... error: corresponding_files.csv. It is corresponding_files.xml...
def get_path_coresponding_pieces():
	mypath = [CORPUS_PATH+'/','']
	echos = None
	with open(mypath[0]+'corresponding_files.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			if 'echos' == row[0]:
				mypath[1] = row[1]+'/'
				echos = row[1]
				continue
			yield [mypath[0]+mypath[1]+row[0], mypath[0]+mypath[1]+row[1], echos]


def piece_num_in_page(name):
	for pos, i in enumerate(reversed(name)):
			if i == '_':
				return name[len(name)-pos:]



def check_input_values(my_echos, corpus_group, my_corpora, method):
	
	if not isinstance(my_echos, str) and not isinstance(my_echos, list):
		raise TypeError('my_echos variable must be either str or list.')
	if isinstance(my_echos, str) and my_echos != 'all':
		raise ValueError("my_echos:<str> must have the value 'all'.")
	if [] == my_echos:
		raise ValueError('my_echos:<list> cannot be empty')
	if isinstance(my_echos, list) and not set(my_echos).issubset(set(all_echoi)):
		raise ValueError("my_echos:<list> must be a 'subset' of the following list ['echos_a', 'echos_b', 'echos_c', 'echos_d', 'echos_pla', 'echos_plb', 'echos_plc' , 'echos_pld'].")
	
	
	if not isinstance(corpus_group, list):
		raise TypeError('corpus_group variable must be list of strs.')
	if not set(corpus_group).issubset(set(all_corpus_group)):
		raise ValueError("corpus_group list must contain some of the following strs: '1', '2'.")
	
	
	if not isinstance(my_corpora, str) and not isinstance(my_corpora, list):
		raise TypeError('my_corpora variable must be either str or list.')
	if isinstance(my_corpora, str) and my_corpora != 'all':
		raise ValueError("my_corpora:<str> must have the value 'all'.")
	if [] == my_corpora:
		raise ValueError('my_corpora:<list> cannot be empty list.')
	if isinstance(my_corpora, list) and not set(my_corpora).issubset(set(all_corpora)):
		raise ValueError("my_corpora:<list> can take a list which contains some of the following strs 'pro-Karykis','karykis','balasis'.")
	
	
	if not isinstance(method, str):
		raise TypeError('method variable must be str.')
	if  method not in all_methods:
		raise ValueError("method can take an str value. This value must be one of the following 'classical_and_pitch_profile', 'triangles_similarity', 'markov_and_entropies', 'melismaticity', 'print_diagram', 'entropies_over_syllable'.")
	
	
	return True





def create_diagrams(my_echos='all', corpus_group=['1','2'], my_corpora='all', my_scalar_of_pieces=None, simplified=False):
	
	#=====================================checking part========================================================================
	check_input_values(my_echos, corpus_group, my_corpora, method='print_diagram')
	#======================================================================================================================

	
	
	if my_echos == 'all':
		my_echos = copy.deepcopy(all_echoi)

		
	if my_corpora == 'all':
		my_corpora = copy.deepcopy(all_corpora)
	
	
	
	corresponding_file_names = ET.parse(CORPUS_PATH+'/corresponding_files.xml')
	root = corresponding_file_names.getroot()
	pieces = root.findall('piece')
	
	
	
	
	
	for each_piece in pieces:
		if each_piece.find('group').text not in corpus_group:
			continue
			
		if '2' == each_piece.find('group').text:
			suffix = "before_christmass_"		
		elif '1' == each_piece.find('group').text:
			suffix = ''
		
		file_path = CORPUS_PATH+"/"
		
		if simplified == True:
				diagram_path = "simplified_diagrams/diagram_"
		else:
				diagram_path = "diagrams/diagram_"

		
		
		if each_piece.find('echos').text not in my_echos:
			continue
		
		
		
		
		file_path = file_path + suffix
		file_path += str(each_piece.find('echos').text)
		
		diagram_path = diagram_path + suffix
		diagram_path += str(each_piece.find('echos').text)
		
		compositions_set = each_piece.find('compositions')
		
		
		a_heirmos = dict()
		for composition in compositions_set:
			if composition.find('composer').text not in my_corpora:
				continue

			a_heirmos[composition.find('composer').text] = file_path + '/' + composition.find('file_name').text
		
			
			
		corpus = xml_parser.xml_parser(list(a_heirmos.values()))
		
		
		pieces_label = list()
		for a_piece in corpus:
			pieces_label.append(a_piece.cargo.library + ' ' + a_piece.cargo.library_number +' (' + a_piece.cargo.starting_folio + ' ' + piece_num_in_page(a_piece.cargo.file_name) + ')')
		
		
		if None == my_scalar_of_pieces:
			my_scalar_of_pieces = dict()
			for i in a_heirmos.keys():
				my_scalar_of_pieces[i] = 0.0

		
		pp.plot_lines(corpus,
				scalar_of_pieces = my_scalar_of_pieces,
				pieces_label = pieces_label,
				title = corpus[0].cargo.initium,
				figure_path = diagram_path,
				simplified=simplified)



# var: echos = values: ['echos_a', 'echos_b', 'echos_c', 'echos_d', 'echos_pla', 'echos_plb', 'echos_plc' , 'echos_pld'] <list of strs>
#                  OR  'all' <str>

# var: corpus_group = values: ['1', '2'] <list of strings>

# var: corpora = values: ['pro-karykis','karykis','Balasis'] <list of strs>
#                     OR  'all' <str>

# var: my_scalar_of_pieces = values: {"pro-karykis":0.0, 'karykis':0.0, 'balasis':0.0}

# create_diagrams(my_echos='all', corpus_group=['1'], my_corpora='all', my_scalar_of_pieces=None, simplified=False)





def classical_and_pitch_profile():
	if os.path.isfile('./stat_classical_pitch_profile.csv') == True:
		os.remove("stat_classical_pitch_profile.csv")
	if os.path.isfile('./stat_classical_pitch_distribution.csv') == True:
		os.remove("stat_classical_pitch_distribution.csv")
	#(γενικά) στατιστικά σε επίπεδο κομματιού
	for pieces_path in zip(*[iter(get_path_coresponding_pieces())]*16):
		iviron1167 = []
		iviron1101 = []
		for p in pieces_path:
			iviron1101.append(p[0])
			iviron1167.append(p[1])

		corpus1101 = xml_parser.xml_parser(iviron1101)
		corpus1167 = xml_parser.xml_parser(iviron1167)
		
		d = pd.DataFrame(modality.stat_classical_pitch_profile(corpus1101))
		d.to_csv('stat_classical_pitch_profile.csv',mode='a', header=True)
		d = pd.DataFrame(modality.stat_classical_pitch_profile(corpus1167))
		d.to_csv('stat_classical_pitch_profile.csv',mode='a', header=True)
		
		d = modality.stat_classical_pitch_distribution(corpus1101)
		d.to_csv('stat_classical_pitch_distribution.csv',mode='a', header=True)
		d = modality.stat_classical_pitch_distribution(corpus1167)
		d.to_csv('stat_classical_pitch_distribution.csv',mode='a', header=True)	

#classical_and_pitch_profile()






def triangles_simiarity():
	file_write = open('triangles_simiarity.txt', 'w', encoding='utf-8')
	
	marked_echos = ''
	for pieces_path in get_path_coresponding_pieces():
		corpus = xml_parser([pieces_path[0], pieces_path[1]])
		temp = peak.common_peaks_with_regression_updated(corpus[0], corpus[1])
		#print(temp)
		if marked_echos != pieces_path[2]:
			marked_echos = pieces_path[2]
			file_write.write(pieces_path[2] + '\n'+ "piece,similar,not_similar\n")
			counter = 1
		
		file_write.write(str(counter)+','+str(temp[0])+','+ str(temp[1]) +'\n')
		counter += 1

	file_write.close()

#triangles_simiarity()





def extract_interval_viewpoint(corpus):  #, simplified = False
	interval_viewpoint_data = []
	for piece in corpus:
		for phrase_or_martyria in piece:
			if isinstance(phrase_or_martyria.cargo, phrase.Phrase):
				for syllable_node in phrase_or_martyria:
					for voiced_sign_node in syllable_node:
						interval_viewpoint_data.extend(voiced_sign_node.cargo.interval)
		interval_viewpoint_data.append(1000)#this number represent the end of the piece
	return interval_viewpoint_data



def extract_pitch_viewpoint(corpus):  #, simplified = False
	pitch_viewpoint_data = []
	for piece in corpus:
		pitch_viewpoint_data.extend(piece.pitch + ["END_OF_PIECE"])
	return pitch_viewpoint_data



#========================================================================================
def extract_pitch_viewpoint_simplified(corpus):
	pitch_viewpoint_data = []
	
	for piece in corpus:
		for phrase_or_martyria in piece:
			if isinstance(phrase_or_martyria.cargo, phrase.Phrase):
				for syllable_node in phrase_or_martyria:
					pitch_viewpoint_data.append(syllable_node.pitch[-1])
		#input(pitch_viewpoint_data)
		pitch_viewpoint_data.append("END_OF_PIECE")
	return pitch_viewpoint_data

def extract_interval_viewpoint_simplified(corpus):
	interval_viewpoint_data = []
	for piece in corpus:
		temp = []
		for phrase_or_martyria in piece:
			if isinstance(phrase_or_martyria.cargo, phrase.Phrase):
				for syllable_node in phrase_or_martyria:
					for voiced_sign_node in syllable_node:
						temp.extend(voiced_sign_node.cargo.interval)
					interval_viewpoint_data.append(sum(temp))
					temp = []
		#input(interval_viewpoint_data)
		interval_viewpoint_data.append(1000)#this number represent the end of the piece
	return interval_viewpoint_data



def extract_melodic_contour_viewpoint_simplified(corpus):
	contour_viewpoint_data = []
	for piece in corpus:
		list_of_intervals_of_syllable = []
		for phrase_or_martyria in piece:
			if isinstance(phrase_or_martyria.cargo, phrase.Phrase):
				for syllable_node in phrase_or_martyria:
					for voiced_sign_node in syllable_node:
						list_of_intervals_of_syllable.extend(voiced_sign_node.cargo.interval)
					sum_of_intervals_of_a_syllable = sum(list_of_intervals_of_syllable)
					if sum_of_intervals_of_a_syllable == 0:
						contour_viewpoint_data.append('.')
					if sum_of_intervals_of_a_syllable < 0:
						contour_viewpoint_data.append('-')
					if sum_of_intervals_of_a_syllable > 0:
						contour_viewpoint_data.append('+')
					list_of_intervals_of_syllable = []
		#input(contour_viewpoint_data)
		contour_viewpoint_data.append("END_OF_PIECE")
	return contour_viewpoint_data
#=======================================================================================





def extract_voice_id_viewpoint(corpus):
	interval_voice_id_data = []
	for piece in corpus:
		for phrase_or_martyria in piece:
			if isinstance(phrase_or_martyria.cargo, phrase.Phrase):
				for syllable_node in phrase_or_martyria:
					'''
					for voiced_sign_node in syllable_node:
						interval_voice_id_data.extend(voiced_sign_node.cargo.user_value)
					'''
					#Αντικατέστησα τις δύο παραπάνω γραμμές με τις δύο από κάτω για να σπάσει τα κεντήματα από τα άλλα σημάδια στα Collocations
					temp = tonoi.get_syllable_voiced_id(syllable_node).split(tonoi.DELIMITER)
					interval_voice_id_data.extend(temp)
					#========================================================================
		interval_voice_id_data.append('END_OF_PIECE')
		#print(interval_voice_id_data)
	return interval_voice_id_data



# Τα θέλει ένα list με τη σειρά.
# calculate the kl divergence
def kl_divergence(p, q):
	return sum(p[i] * math.log2(p[i]/q[i]) for i in range(len(p)))





def cross_entropy_and_KL_divergence(m1, m2):
	total_sum_cross_entropy = 0.0
	total_sum_KL_divergence = 0.0
	for index in m1.index:
		for column in m1.columns:
			total_sum_cross_entropy += m1[column][index]* math.log(m2[column][index],2)
			total_sum_KL_divergence += m1[column][index]* math.log(m1[column][index]/m2[column][index],2)
	return (total_sum_cross_entropy * (-1), total_sum_KL_divergence)





def create_couples_for_comparisons(corpora1, corpora2):
	doubles_for_comparisons = []
	for i in list(product(corpora1,corpora2)):
		if i[0] == i[1]:
			continue
		temp = [i[0], i[1]]
		temp.sort()
		if temp in doubles_for_comparisons:
			continue
		doubles_for_comparisons.append(temp)
	
	return doubles_for_comparisons




def count_smoothing_and_not_values(adataframe, smoothing=1.0):
	smoothed_cells = 0
	total_cells = 0
	for _, value_of_columns in adataframe.iteritems():
		for a_value in value_of_columns:
			total_cells += 1
			if smoothing == a_value:
				smoothed_cells += 1
	
	print("smoothed_cells =", smoothed_cells)
	print("total_cells =", total_cells)
	
	print("smoothed_cells % =", (smoothed_cells*100)/total_cells)



def general_interface(my_echos, corpus_group, my_corpora, method, **kwargs):
	
	#=====================================checking part====================================================================
	check_input_values(my_echos, corpus_group, my_corpora, method)
	#======================================================================================================================
	
	#delete previous files
	if os.path.isfile('./classical_approach.csv') == True:
		os.remove("classical_approach.csv")
	if os.path.isfile('./pitch_profile_approach.csv') == True:
		os.remove("pitch_profile_approach.csv")
	
	
	if os.path.isfile('./triangles_similarity_data.csv') == True:
		os.remove("triangles_similarity_data.csv")
	
	
	if os.path.isfile('./melismaticity.csv') == True:
		os.remove("melismaticity.csv")
	data = dict()
	
	
	
	
	
	
	
	if my_echos == 'all':
		my_echos = copy.deepcopy(all_echoi)

		
	if my_corpora == 'all':
		my_corpora = copy.deepcopy(all_corpora)
	
	#read the xml corresponding_files in order to parse the files
	corresponding_file_names = ET.parse(CORPUS_PATH+'/corresponding_files.xml')
	root = corresponding_file_names.getroot()
	pieces = root.findall('piece')
	
	
	
	
	
	if 'classical_and_pitch_profile' == method or 'markov_and_entropies' == method or 'melismaticity' == method or 'entropies_over_syllable':
		for each_piece in pieces:
			
			
			#About group
			piece_group = each_piece.find('group')
			if None == piece_group:
				raise ValueError("I couldn't manage to find the group tag. Cheack your XML file.")
			
			if piece_group.text not in corpus_group:
				continue
			
			if None == data.get(piece_group.text):
				data[piece_group.text] = dict()
			
				
			
			if piece_group.text == '1':
				prefix_path = CORPUS_PATH+'/'
			elif piece_group.text == '2':
				prefix_path = CORPUS_PATH+'/before_christmass_'
			

			
			#About echos
			piece_echos = each_piece.find('echos')
			if None == piece_echos:
				raise ValueError("I couldn't manage to find the echos tag. Cheack your XML file.")
			
			if piece_echos.text not in my_echos:
				continue
			
			if None == data[piece_group.text].get(piece_echos.text):
				data[piece_group.text][piece_echos.text] = dict()
			
			compositions_tag = each_piece.find('compositions')
			compositions = compositions_tag.findall('composition')
			for composition in compositions:

				for composer_and_file_name in composition:
					if composer_and_file_name.tag == 'composer':
						if composer_and_file_name.text not in my_corpora:
							break
						if None == data[piece_group.text][piece_echos.text].get(composer_and_file_name.text):
							data[piece_group.text][piece_echos.text][composer_and_file_name.text] = list()
						temp = composer_and_file_name.text
					if composer_and_file_name.tag == 'file_name':
						data[piece_group.text][piece_echos.text][temp].append(prefix_path+piece_echos.text+'/'+composer_and_file_name.text)
			
	
	
	if 'triangles_similarity' == method:
		d = pd.DataFrame( columns=['similar', 'not_similar', 'used_triangles', 'not_used_triangles'])
		
		for each_piece in pieces:
			
			#About group
			piece_group = each_piece.find('group')
			if None == piece_group:
				raise ValueError("I couldn't manage to find the group tag. Check your XML file.")
			
			if piece_group.text not in corpus_group:
				continue
			
			
			if piece_group.text == '1':
				prefix_path = CORPUS_PATH+'/'
			elif piece_group.text == '2':
				prefix_path = CORPUS_PATH+'/before_christmass_'
			
			
			#About echos
			piece_echos = each_piece.find('echos')
			if None == piece_echos:
				raise ValueError("I couldn't manage to find the echos tag. Check your XML file.")
			
			if piece_echos.text not in my_echos:
				continue
			
			''''''
			with open('triangles_similarity_data.csv', mode='a', encoding='utf-8') as f_triangles_similarity:
				f_triangles_similarity.write(piece_group.text +','+ piece_echos.text + '\n')
				f_triangles_similarity.write(',,similar,not_similar,used_triangles,not_used_triangles\n')
			
			
			
			compositions_tag = each_piece.find('compositions')
			compositions = compositions_tag.findall('composition')
			compositions_paths={}
			
				
			for composition in compositions:
				
				for composer_and_file_name in composition:
					if composer_and_file_name.tag == 'composer':
						if composer_and_file_name.text not in my_corpora:
							break
						
						compositions_paths[composer_and_file_name.text] = ''
						temp = composer_and_file_name.text
						
					if composer_and_file_name.tag == 'file_name':
						compositions_paths[temp] = prefix_path+piece_echos.text + '/' + composer_and_file_name.text
			
			
			
			from itertools import combinations
			teams = list(compositions_paths.keys())
			product = [items for items in combinations(teams, r=2)]
			
			
			for a_corpus in product:
				#print([ compositions_paths[a_corpus[0]], compositions_paths[a_corpus[1]] ])
				with open('triangles_similarity_data.csv', mode='a', encoding='utf-8') as f_triangles_similarity:
					
					
					corpus = xml_parser.xml_parser([ compositions_paths[a_corpus[0]], compositions_paths[a_corpus[1]] ])
					
					
					#print(a_corpus[0], a_corpus[1])
					common_peaks_results = peak.common_peaks_with_regression_updated(corpus[0], corpus[1])
					
					if a_corpus[0]+' -- '+ a_corpus[1] not in d.index:
						d.loc[a_corpus[0]+' -- '+ a_corpus[1]] = [0,0,0,0]
					
					d['similar'][a_corpus[0]+' -- '+ a_corpus[1]] += common_peaks_results[0]
					d['not_similar'][a_corpus[0]+' -- '+ a_corpus[1]] += common_peaks_results[1]
					d['used_triangles'][a_corpus[0]+' -- '+ a_corpus[1]] += common_peaks_results[2]['used_triangles']
					d['not_used_triangles'][a_corpus[0]+' -- '+ a_corpus[1]] += common_peaks_results[2]['not_used_triangles']
					
					
					
					f_triangles_similarity.write(a_corpus[0] +','+ a_corpus[1] + ','+ str(common_peaks_results[0])+',' +str(common_peaks_results[1]) + 
								  ','+str(common_peaks_results[2]['used_triangles'])+ ','+str(common_peaks_results[2]['not_used_triangles'])+'\n')
					del(common_peaks_results)
					
					'''
					#print(a_corpus[1], a_corpus[0])
					common_peaks_results = peak.common_peaks_with_regression_updated(corpus[1], corpus[0])
					
					f_triangles_similarity.write(a_corpus[1] +','+ a_corpus[0] + ','+ str(common_peaks_results[0])+',' +str(common_peaks_results[1]) + 
								  ','+str(len(common_peaks_results[2]['not_corresponding_triangles1']))+ ','+str(len(common_peaks_results[2]['not_corresponding_triangles2']))+ '\n')
					del(common_peaks_results)
					'''
		for index in d.index:
			similar_and_not_similar = d['similar'][index] + d['not_similar'][index]
			d['similar'][index] /= similar_and_not_similar
			d['not_similar'][index] /= similar_and_not_similar 
			
			used_and_not_used = d['used_triangles'][index] + d['not_used_triangles'][index]
			d['used_triangles'][index] /= used_and_not_used
			d['not_used_triangles'][index] /= used_and_not_used 
			
			d['similar'][index] *= d['used_triangles'][index]
			d['not_similar'][index] *= d['used_triangles'][index]
		
		del(d["used_triangles"])
		d = d*100
		d = d.astype(float).round(1)
		d.to_csv('triangles_similarity_stats.csv')
		
	
	#run the choosen approach==============================================================================================
	if 'classical_and_pitch_profile' == method:
		f_classical_approach =  open('classical_approach.csv', mode='a') 
		f_pitch_profile_approach = open('pitch_profile_approach.csv', mode='a')
		for k_groups, v_groups in data.items():
			for k_echos, v_echos in v_groups.items():
				for k_corpus, v_corpus in v_echos.items():
					temp_corpus = xml_parser.xml_parser(v_corpus)
					if [] == temp_corpus:
						continue
							
					f_classical_approach.write('group '+k_groups+','+k_echos+','+k_corpus+'\n')
					f_pitch_profile_approach.write('group '+k_groups+','+k_echos+','+k_corpus+'\n')
							
					d = modality.stat_classical_pitch_distribution(temp_corpus)
					d.to_csv(f_classical_approach, mode='a', header=True, line_terminator='\n')
					d = pd.DataFrame(modality.stat_classical_pitch_profile(temp_corpus))
					d.to_csv(f_pitch_profile_approach, mode='a', header=True, line_terminator='\n')
					
					
					pitch_dict_group_by_phrase, pitch_distribution_group_by_phrase, my_phrases = modality.stat_phrase_classical_pitch_distribution(temp_corpus)
					
					
					f_classical_approach.write('\n\n\n')
					f_pitch_profile_approach.write('\n\n\n')
					
					'''
					for corpus_name, results in pitch_dict_group_by_phrase.items():
						pitch_dict_group_by_phrase[corpus_name].to_csv('phrase_classical_'+corpus_name+'.csv', mode='a')
						pitch_distribution_group_by_phrase[corpus_name].to_csv('phrase_profile_'+corpus_name+'.csv', mode='a')
					'''
					
					
		f_classical_approach.close()
		f_pitch_profile_approach.close()
		
		pass
		#visualization.visualize(temp_corpus[7])
	
	#visualization.visualize(my_phrases)
	
	
	
	
	
	if 'melismaticity' == method:
		melismaticity_approach =  open('melismaticity.csv', mode='a')
		
		for k_groups, v_groups in data.items():
			for k_echos, v_echos in v_groups.items():
				
				melismaticity_approach.write('group '+k_groups+','+k_echos+'\n')
				header = False
				
				dict_num_pitch_echos = {}

				
				for k_corpus, v_corpus in v_echos.items():
					temp_corpus = xml_parser.xml_parser(v_corpus)
					if [] == temp_corpus:
						continue
					
					
					

					total_average, list_melismaticity_average, list_num_pitch = melismaticity.find_melismaticity_in_list_of_pieces(temp_corpus)

					dict_num_pitch_echos[k_corpus] = dict(Counter(list_num_pitch))
					
					str_num_of_piece = ''
					str_list_melismaticity_average = ''
					
					for num, piece_average_melismaticity in enumerate(list_melismaticity_average):
						str_list_melismaticity_average += str(piece_average_melismaticity) + ','
						str_num_of_piece += str(num+1) + ','

				
					if header == False:
						melismaticity_approach.write(","+" melismaticity_average" +','+ str_num_of_piece + '\n')
						header = True
					
					
					melismaticity_approach.write(k_corpus+","+str(total_average) +','+  str_list_melismaticity_average + '\n')
				print(dict_num_pitch_echos)
				#εδώ θα προσθέσω κώδικα αν χρειστεί για να βγάλω κατανομή στο melismaticity
				melismaticity_approach.write('\n\n\n')
					
					
		melismaticity_approach.close()



	
	if 'markov_and_entropies' == method:	
		if os.path.isfile('./markov_and_entropies/cross-entropy and kld.txt') == True:
			os.remove("cross-entropy and kld.txt")
		
		
		mypath = './markov_and_entropies/'
		files_name = [os.path.join(mypath, f) for f in os.listdir(mypath) if (f.startswith('markov_pro-karykis_') or f.startswith('markov_karykis_') or f.startswith('markov_balasis_') ) and f.endswith('.csv')]
		for file in files_name:
			os.remove(file)
		
		
		simplified = False #add this line code for simplification flag============================================
		
		
		
		for key_kwargs, value_kwargs in kwargs.items():
			if key_kwargs == 'viewpoint':
				viewpoint=value_kwargs
			if key_kwargs == 'context':
				context = value_kwargs
			
			#============add for simplification=======================================================================
			if key_kwargs == 'simplified':
				if not isinstance(value_kwargs, bool):
					raise TypeError("The simplification attribute must be boolean value.")
				simplified = value_kwargs
		if simplified == True and context == "voice_id":
			raise ValueError('You cannot create markov model in voice_id attribute with simplified data')
			
		
		
		
		for k_groups, v_groups in data.items():
			for k_echos, v_echos in v_groups.items():
				
				
				with open('KLd__JSd__'+k_echos+'.csv', 'a') as write_kld:
					write_kld.write(viewpoint + ',' +str(context+1) + '-grams\n')
					
				
				markov_corpora = dict()
				for k,v in v_echos.items():
					markov_corpora[k] = None
				
				for k_corpus, v_corpus in v_echos.items():
					temp_corpus = xml_parser.xml_parser(v_corpus)
					if [] == temp_corpus:
						continue
		
					if simplified == False: #I add this if-else statement as decition step
						if viewpoint == 'interval':
							viewpoint_seq = extract_interval_viewpoint(temp_corpus)
						elif viewpoint == 'pitch':
							viewpoint_seq = extract_pitch_viewpoint(temp_corpus)
						elif viewpoint == 'voice_id':
							viewpoint_seq = extract_voice_id_viewpoint(temp_corpus)
						
					#==========================================================
					else:
						if viewpoint == 'interval':
							viewpoint_seq = extract_interval_viewpoint_simplified(temp_corpus)
						elif viewpoint == 'pitch':
							viewpoint_seq = extract_pitch_viewpoint_simplified(temp_corpus)
						elif viewpoint == 'contour':
							viewpoint_seq = extract_melodic_contour_viewpoint_simplified(temp_corpus)
					#===========================================================
					
					
					
					
					
					
						
					markov_corpora[k_corpus] = mft.dynamic_transition_matrix(viewpoint_seq, order=context)
					initial_count = 1.0 # βάζω 1.0 για να κάνω Laplace Smoothing
				
				#=================================================================================
				#find the couples that we want to do Smoothing and to compute the KL-divergence and the JS-divergence
				list_couples = create_couples_for_comparisons(my_corpora,my_corpora)
				
				
				
				#Smoothing the couples and then calculate the KL-divergence and the JS-divergence
				for couple in list_couples:
					
					
					temp_corpus0 = markov_corpora[couple[0]].copy(deep=True)
					temp_corpus1 = markov_corpora[couple[1]].copy(deep=True)
					
					# add the appropriate columns to each markov
					i_have_to_add_to_col1 = temp_corpus0.columns.difference(temp_corpus1.columns)
					i_have_to_add_to_col0 = temp_corpus1.columns.difference(temp_corpus0.columns)
					for column in i_have_to_add_to_col0:
						num_of_rows = len(temp_corpus0)
						temp_corpus0[column] = list([initial_count for j in range(num_of_rows)])
					for column in i_have_to_add_to_col1:
						num_of_rows = len(temp_corpus1)
						temp_corpus1[column] = list([initial_count for j in range(num_of_rows)])
					temp_corpus0 = temp_corpus0.sort_index(axis=1)
					temp_corpus1 = temp_corpus1.sort_index(axis=1)
					
					
					# add the appropriate rows to each markov
					i_have_to_add_to_row1 = temp_corpus0.index.difference(temp_corpus1.index)
					i_have_to_add_to_row0 = temp_corpus1.index.difference(temp_corpus0.index)
					for row in i_have_to_add_to_row0:
						temp_row = list([initial_count for j in range(len(temp_corpus0.columns))])
						temp_corpus0.loc[row] = temp_row
					for row in i_have_to_add_to_row1:
						temp_row = list([initial_count for j in range(len(temp_corpus1.columns))])
						temp_corpus1.loc[row] = temp_row
					temp_corpus0 = temp_corpus0.sort_index(ascending=True)
					temp_corpus1 = temp_corpus1.sort_index(ascending=True)
					
					

					
					
					# convert the frequency table to relative frequency	
					total = temp_corpus0.sum()
					for element in temp_corpus0.columns:
						temp_corpus0[element] = temp_corpus0.div(total[element])[element]
					total = temp_corpus1.sum()
					for element in temp_corpus1.columns:
						temp_corpus1[element] = temp_corpus1.div(total[element])[element]
					
					#==========================================================
					#υπολογισμός των heatmaps
					#temp_corpus0.to_csv('heatmaps'+'/'+k_echos+'/'+'matrix_'+couple[0]+'_'+str(context+1)+'grams.csv')
					ax = sns.heatmap(abs(temp_corpus1-temp_corpus0), xticklabels=False,yticklabels=False, vmin=0.0, vmax=1.0)
					fig = ax.get_figure()
					fig.savefig('heatmaps/voiced_id'+'/'+k_echos+'/'+couple[1]+'--'+couple[0]+'_'+str(context+1)+"grams.png")
					fig.clf()
					
					#==========================================================
					
					
					# convert the table to vector
					temp0 = np.reshape(np.array(temp_corpus0), -1)
					temp1 = np.reshape(np.array(temp_corpus1), -1)
					
					
					# calculate kl_divergence and js_divergence
					kl_divergence_corpus0_corpus1 =  round(kl_divergence(temp0, temp1), 2)
					kl_divergence_corpus1_corpus0 =  round(kl_divergence(temp1, temp0), 2)
					
					js_divergence = round(distance.jensenshannon(temp0, temp1, base=2), 3)

					
					
					
					
					with open('KLd__JSd__'+k_echos+'.csv', 'a') as write_kld:
						write_kld.write(
							'KLd: '+ couple[0] + ' -- '+couple[1] + ',' + str(kl_divergence_corpus0_corpus1) + \
								',KLd: ' + couple[1] + ' -- '+couple[0] + ',' + str(kl_divergence_corpus1_corpus0) + \
									',,JSd: ' + couple[1] + ' -- '+couple[0] +','+ str(js_divergence)+'\n'
									)
				
					
				
		with open('KLd__JSd__'+k_echos+'.csv', 'a') as write_kld:
			write_kld.write('\n')
				
				
				
				
				
				
				

	
	
	
	
	
	
	if 'entropies_over_syllable' == method:	
		if os.path.isfile('./entropies_syllable/cross-entropy and kld.txt') == True:
			os.remove("cross-entropy and kld.txt")
		
		mypath = './entropies_syllable/'
		files_name = [os.path.join(mypath, f) for f in os.listdir(mypath) if (f.startswith('markov_pro-karykis_') or f.startswith('markov_karykis_') or f.startswith('markov_balasis_') ) and f.endswith('.csv')]
		for file in files_name:
			os.remove(file)
		
		
		for key_kwargs, value_kwargs in kwargs.items():
			if 'viewpoint' == key_kwargs :
				viewpoint=value_kwargs
		
		
		
		for k_groups, v_groups in data.items():
			for k_echos, v_echos in v_groups.items():

				markov_corpora = dict()
				for k,v in v_echos.items():
					markov_corpora[k] = None
				
				for k_corpus, v_corpus in v_echos.items():
					if [] == v_corpus:
						continue
					tonoi_dataFrame, tonoi_stats, melismaticity_ = tonoi.find_tonoi_frequency(v_corpus, viewpoint)
					
					print(k_corpus)
					print(tonoi_dataFrame)
					print('melismaticity =', melismaticity_)
					print("\n\n")
					tonoi_dataFrame.to_csv(mypath +"group_"+k_groups+'_'+k_corpus+'_'+str(k_echos)+'.txt')
					
					temp_path = mypath +"group_"+k_groups+'_'+k_corpus+'_'+str(k_echos)+'_'+'tonoi_stats'+'.csv'
					
					tonoi_stats.to_csv(temp_path)
					
					
					#append the csv file (tonoi_stats) with melismaticity indicator
					with open(temp_path, "a") as f:
						f.write('\n\n')
						f.write('melismaticity\n')
						f.write(str(melismaticity_))
					
					
					
					#print(tonoi_dataFrame.loc['a',:])
				
					



# acceptable arguments: echos = values: ['echos_a', 'echos_b', 'echos_c', 'echos_d', 'echos_pla', 'echos_plb', 'echos_plc' , 'echos_pld'] <list of strs>
#                  OR  'all' <str>

# acceptable arguments: corpus_group = values: ['1', '2'] <list of strings>

# acceptable arguments: corpora = values: ['pro-karykis','karykis','balasis'] <list of strs>
#                     OR  'all' <str>

# acceptable arguments: methods = values: 'classical_and_pitch_profile', 'triangles_similarity', 'markov_and_entropies', 'melismaticity', 'entropies_over_syllable' <str>

# ADDITIONAL acceptable arguments for markov_and_entropies and entropies_over_syllable methods
# viewpoint='interval', or 'pitch', or 'voice_id' <str> AND context = <int>

	
''''''
general_interface(my_echos=['echos_a'],
				  corpus_group = ['1'],
				  my_corpora = 'all',
				  method = 'entropies_over_syllable', viewpoint='voice_id')











'''
#=======================================================================================================================================
# draft export byzantine musical pieces from KR to Western staf.


def kr_to_western_staff():
	corresponding_file_names = ET.parse(CORPUS_PATH+'/corresponding_files.xml')
	root = corresponding_file_names.getroot()
	pieces = root.findall('piece')
	corpus = []
	for each_piece in pieces:	
		if '2' == each_piece.find('group').text:
			suffix = "before_christmass_"		
		elif '1' == each_piece.find('group').text:
			suffix = ''
		
		file_path = CORPUS_PATH+"/"
		file_path = file_path + suffix
		file_path += str(each_piece.find('echos').text)
		
		if suffix != "before_christmass_":
			lilypond_path = os.path.join(CORPUS_PATH, suffix, each_piece.find('echos').text)
		else:
			lilypond_path = os.path.join(CORPUS_PATH, suffix + each_piece.find('echos').text)
		
		compositions_set = each_piece.find('compositions')
		
		for composition in compositions_set:
			
			piece = xml_parser.xml_parser([os.path.join(lilypond_path, composition.find('file_name').text)])
			print(piece[0])
			
			filename = piece[0].cargo.file_name
			lp_notes, lp_lyrics, header = b2s.byzmusic2staff(piece[0])
			
			with open(os.path.join('lilypond_form', lilypond_path ,filename)+'.ly', 'w', encoding='utf-8') as f:
				f.write(b2s.create_lilypond_score_string(lp_notes, lp_lyrics, header))
'''




#kr_to_western_staff()

#=======================================================================================================================================
'''
my_echos1='all'
print(my_echos1)
for i in range(1, 7):
	print('order =', i)
	general_interface(my_echos=my_echos1,
					  corpus_group = ['1'],
					  my_corpora = 'all',
					  method = 'markov_and_entropies', viewpoint='voice_id', context = i, simplified=False)
'''








#=======================================================================================================================================
# var: echos = values: ['echos_a', 'echos_b', 'echos_c', 'echos_d', 'echos_pla', 'echos_plb', 'echos_plc' , 'echos_pld'] <list of strs>
#                  OR  'all' <str>

# var: corpus_group = values: ['1', '2'] <list of strings>

# var: corpora = values: ['pro-karykis','karykis','Balasis'] <list of strs>
#                     OR  'all' <str>

# var: my_scalar_of_pieces = values: {"pro-karykis":0.0, 'karykis':0.0, 'balasis':0.0}

# create_diagrams(my_echos=['echos_d'], corpus_group=['1'], my_corpora=['pro-karykis', 'karykis'], my_scalar_of_pieces=None, simplified=True)

#=======================================================================================================================================


#read the xml corresponding_files in order to parse the files
'''

def find_composer_id(composer_name):
	if composer_name=='pro-karykis':
		return 0
	elif composer_name=='karykis':
		return 1
	return 2




import pprint
pp = pprint.PrettyPrinter(indent=4)

corresponding_file_names = ET.parse(CORPUS_PATH+'/corresponding_files.xml')
root = corresponding_file_names.getroot()
pieces = root.findall('piece')



data = []

#print(pieces)
for each_piece in pieces:
	piece_group = each_piece.find('group')
	piece_echos = each_piece.find('echos')
	piece_compositions = each_piece.find('compositions')
	for each_composition in piece_compositions:
		piece_composer = each_composition.find('composer')
		piece_file_name = each_composition.find('file_name')
		if piece_group.text == '2':
			
			path = CORPUS_PATH+'/before_christmass_echos_a/'+piece_file_name.text
			#input('\n\n'+path+'\n\n')
			parsed_music_piece = xml_parser.xml_parser([path])
			
			data.append([piece_group.text, piece_echos.text, piece_composer.text, find_composer_id(piece_composer.text), " ".join(parsed_music_piece[0].pitch)  ])
			continue
		
		path = CORPUS_PATH+'/'+piece_echos.text+'/'+piece_file_name.text
		parsed_music_piece = xml_parser.xml_parser([path])
		
		data.append([piece_group.text, piece_echos.text, piece_composer.text, find_composer_id(piece_composer.text), " ".join(parsed_music_piece[0].pitch)   ])
		
pp.pprint(data)

from sklearn.feature_extraction.text import CountVectorizer
dataframe_data = pd.DataFrame(data, columns=['group', 'echos', 'composer', 'composer_id', 'pitches'])



count_vect = CountVectorizer(lowercase=False, stop_words=[' '], token_pattern=r"'*\w+'*")
X_train_counts = count_vect.fit_transform(list(dataframe_data['pitches']))
print(count_vect.get_feature_names())




from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print('TF-IDF')
print(X_train_tfidf)


from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
text_clf = Pipeline([
	('vect', CountVectorizer()),
	('tfidf', TfidfTransformer()),
	('clf', MultinomialNB()),
])
text_clf.fit(dataframe_data['pitches'], dataframe_data['composer_id'])


import numpy as np

#docs_test = ['va aa ba ca va ea va ag av av va','Aa Aa aa a c d da da ae ea ea ea','Aa Aa Aa a Ac d da da ae ea ea ead']

#predicted = text_clf.predict(docs_test)
#print(np.mean(predicted == [0,1,2]))

from sklearn import metrics
print(metrics.classification_report([0,1,2], predicted, target_names=['pro-karykis', 'karykis', 'balasis']))

print(metrics.confusion_matrix([0,1,2], predicted))

'''



import pprint
pp = pprint.PrettyPrinter(indent=4)



def find_path(group, echos, file_name, CORPUS_PATH):
	if '2' == group:
		suffix = "before_christmass_"		
	elif '1' == group:
		suffix = ''
	
	return os.path.join(CORPUS_PATH, suffix+echos,file_name)


def tabularize_KR(a_KR_file):
	music_piece = {
		'voiced_units':[],
		'intervals':[],
		'pitches':[],
		'syllables':[],
		'index':[]
		}
	
	pos = -1
	for node_phrase_martyria in a_KR_file:
		if not isinstance(node_phrase_martyria.cargo, phrase.Phrase):
			continue
		
		for node_syllable in node_phrase_martyria:
			pos += 1
			len_pitches_per_syllable = 0
			
			
			for node_voiced_units in node_syllable:
				voiced_unit = node_voiced_units.cargo
				
				music_piece["intervals"].extend(voiced_unit.interval)
				music_piece["pitches"].extend(node_voiced_units.pitch)
				
				len_pitches = len(node_voiced_units.pitch)
				user_value_list = [None for i in range(len_pitches)]
				user_value_list[-1] = voiced_unit.user_value[-1]
				music_piece["voiced_units"].extend(user_value_list)
				
				len_pitches_per_syllable += len_pitches
			
			step = 1/len_pitches_per_syllable
			indexes_list = [round(pos + i*step,2) for i in range(1,len_pitches_per_syllable+1)]
			music_piece['index'].extend(indexes_list)
			
			syllable = [None for i in range(len_pitches_per_syllable)]
			syllable[-1] = node_syllable.cargo.syllable
			music_piece['syllables'].extend(syllable)
			
	return music_piece




corpus = []
#read the xml corresponding_files in order to parse the files
corresponding_file_names = ET.parse(CORPUS_PATH+'/corresponding_files.xml')
root = corresponding_file_names.getroot()
piece_list = root.findall('piece')
for piece_bunch in piece_list:
	
	piece_metadata = {
		"group": None,
		"echos": None,
		"composer": None,
		"file_name": None,
		"full_path": None,
		"data": None,
		}
	
	
	
	piece_metadata['group'] = piece_bunch.find('group').text
	piece_metadata["echos"] = piece_bunch.find('echos').text
	
	compositions_bunch = piece_bunch.find("compositions")
	composition_bunch = compositions_bunch.findall('composition')
	for a_composition_bunch in composition_bunch:
		piece_metadata['composer'] = a_composition_bunch.find('composer').text
		piece_metadata['file_name'] = a_composition_bunch.find('file_name').text
		
		target_full_path = find_path(
			piece_metadata['group'],
			piece_metadata["echos"],
			piece_metadata['file_name'],
			CORPUS_PATH
			)
		piece_metadata['full_path'] = target_full_path
		
		a_piece = xml_parser.xml_parser([piece_metadata['full_path']])[0]
		piece_dict = tabularize_KR(a_piece)
		piece_metadata['data'] = piece_dict
		
	corpus.append(piece_metadata)

import gzip
import pickle
with gzip.open("corpus.gz", "w") as wf:
	pickle.dump(corpus,wf)











'''
if 'classical_and_pitch_profile' == method or 'markov_and_entropies' == method or 'melismaticity' == method or 'entropies_over_syllable':
	for each_piece in pieces:
		
		
		#About group
		piece_group = each_piece.find('group')
		if None == piece_group:
			raise ValueError("I couldn't manage to find the group tag. Cheack your XML file.")
		
		if piece_group.text not in corpus_group:
			continue
		
		if None == data.get(piece_group.text):
			data[piece_group.text] = dict()
		
			
		
		if piece_group.text == '1':
			prefix_path = CORPUS_PATH+'/'
		elif piece_group.text == '2':
			prefix_path = CORPUS_PATH+'/before_christmass_'
		

		
		#About echos
		piece_echos = each_piece.find('echos')
		if None == piece_echos:
			raise ValueError("I couldn't manage to find the echos tag. Cheack your XML file.")
		
		if piece_echos.text not in my_echos:
			continue
		
		if None == data[piece_group.text].get(piece_echos.text):
			data[piece_group.text][piece_echos.text] = dict()
		
		compositions_tag = each_piece.find('compositions')
		compositions = compositions_tag.findall('composition')
		for composition in compositions:

			for composer_and_file_name in composition:
				if composer_and_file_name.tag == 'composer':
					if composer_and_file_name.text not in my_corpora:
						break
					if None == data[piece_group.text][piece_echos.text].get(composer_and_file_name.text):
						data[piece_group.text][piece_echos.text][composer_and_file_name.text] = list()
					temp = composer_and_file_name.text
				if composer_and_file_name.tag == 'file_name':
					data[piece_group.text][piece_echos.text][temp].append(prefix_path+piece_echos.text+'/'+composer_and_file_name.text)


'''

















