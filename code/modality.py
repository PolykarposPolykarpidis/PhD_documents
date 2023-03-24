# -*- coding: utf-8 -*-
from abcd import pitch_list
from byzTree import getPosPitchList
import phrase

import numpy as np
import pandas as pd




pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import unittest


'''
Classical approach
-----------------------
- base
- final_pitch
- highest_pitch
- lowest_pitch
-----------------------
'''

def stat_classical_pitch_profile(a_corpus):
	if type(a_corpus) != list:
		raise TypeError("The stat_classical_pitch_profile function argument must be a list of musical pieces.")
	if len(a_corpus) == 0 :
		raise IndexError("The list of musical pieces must contain at least a piece")
	
	
	d = pd.DataFrame(0, index=['base','final_pitch','highest_pitch','lowest_pitch'], columns=pitch_list)
	
	for each_piece in a_corpus:
		base_pitch, final_pitch, lowest_pitch, highest_pitch = classical_pitch_profile(each_piece)
		
		d[base_pitch]['base'] = d[base_pitch]['base'] + 1
		d[final_pitch]['final_pitch'] = d[final_pitch]['final_pitch'] + 1
		d[lowest_pitch]['lowest_pitch'] = d[lowest_pitch]['lowest_pitch'] + 1
		d[highest_pitch]['highest_pitch'] = d[highest_pitch]['highest_pitch'] + 1
	
	#d = d.div(len(a_corpus))   # μετατροπή των απόλυτων συχνοτήτων σε σχετικές συχνότητες
	return d





def classical_pitch_profile(a_piece):
	base_pitch = a_piece.child.pitch[-1]
	final_pitch = a_piece.pitch[-1]
	lowest_pitch = pitch_list[-1]
	highest_pitch = pitch_list[0]
	
	for each_pitch in a_piece.pitch:
		#find the lowest_pitch of the piece
		if getPosPitchList(each_pitch)<getPosPitchList(lowest_pitch):
			lowest_pitch = each_pitch
		
			#find the highest_pitch of the piece
		if getPosPitchList(each_pitch)>getPosPitchList(highest_pitch):
			highest_pitch = each_pitch
		
	return base_pitch, final_pitch, lowest_pitch, highest_pitch




'''
pitch distribution of the pieces
-----------------------
- pitch distribution
-----------------------
'''

def stat_classical_pitch_distribution(a_corpus):
	d = pd.DataFrame(0, index=['num_of'], columns=pitch_list)
	
	for each_piece in a_corpus:
		d = d + classical_pitch_distribution(each_piece)
	
	
	d.to_pickle("pandas_data_method2/"+"echos "+each_piece.cargo.mode+" "+each_piece.cargo.composer[:7]+".pkl")
	num_of_pitches = d.to_numpy().sum()
	d = d.div(num_of_pitches)
	
	return d



def classical_pitch_distribution(a_piece):
	d = pd.DataFrame(0, index=['num_of'], columns=pitch_list)
	
	
	
	for each_pitch in a_piece.pitch:
		d[each_pitch]['num_of'] = d[each_pitch]['num_of'] + 1
	return d





'''
Classical approach on the phrase level
-----------------------
- base
- final_pitch
- highest_pitch
- lowest_pitch
-----------------------
'''



def stat_phrase_classical_pitch_distribution(a_corpus):
	pitch_dict_group_by_phrase = dict()
	pitch_distribution_group_by_phrase = dict()
	
	my_phrases = []
	
	for each_piece in a_corpus:
		for each_phrase_or_martyria in each_piece:
			if type(each_phrase_or_martyria.cargo) == phrase.Phrase:
				
				base_pitch, final_pitch, lowest_pitch, highest_pitch = phrase_classical_pitch_profile(each_phrase_or_martyria)
				
				phrase_pitch_distribution = classical_pitch_distribution(each_phrase_or_martyria)
				
				
				if type(pitch_dict_group_by_phrase.get(final_pitch)) == type(None):
					
					pitch_dict_group_by_phrase[final_pitch] = pd.DataFrame(0, index=['base_pitch','final_pitch','highest_pitch','lowest_pitch'], columns=pitch_list)
					
					pitch_distribution_group_by_phrase[final_pitch] = pd.DataFrame(0, index=['num_of'], columns=pitch_list)
					
					
				pitch_dict_group_by_phrase[final_pitch][base_pitch]['base_pitch'] += 1
				pitch_dict_group_by_phrase[final_pitch][final_pitch]['final_pitch'] += 1
				pitch_dict_group_by_phrase[final_pitch][lowest_pitch]['lowest_pitch'] += 1
				pitch_dict_group_by_phrase[final_pitch][highest_pitch]['highest_pitch'] += 1
				
				pitch_distribution_group_by_phrase[final_pitch] = pitch_distribution_group_by_phrase[final_pitch].add(phrase_pitch_distribution, fill_value=0)
				
				
				if final_pitch in ['e', 'f']:
					my_phrases.append(each_phrase_or_martyria)
				''''''
				

	
	
	# μετατροπή από μέτρηση πλήθους σε μέτρηση συχνότητας στο διάστημα [0,1]
	for k,v in pitch_dict_group_by_phrase.items():
		
		pitch_dict_group_by_phrase[k].to_csv('cadence_'+k+'.csv', mode='a')
		pitch_dict_group_by_phrase[k] = v.div(v[k]['final_pitch'])
		
		
		
		pitch_distribution_group_by_phrase[k] = pitch_distribution_group_by_phrase[k].div(pitch_distribution_group_by_phrase[k].to_numpy().sum())
		
		
		
	''''''
	
		
	return pitch_dict_group_by_phrase, pitch_distribution_group_by_phrase, my_phrases
	



'''
pitch distribution of the phrases
-----------------------
- pitch distribution
-----------------------
'''


def phrase_classical_pitch_profile(a_phrase):
	base_pitch = pitch_list[getPosPitchList(a_phrase.child.child.pitch[0])-a_phrase.child.child.cargo.interval[0]]
	final_pitch = a_phrase.pitch[-1]
	
	lowest_pitch = pitch_list[-1]
	highest_pitch = pitch_list[0]
	
	for each_pitch in a_phrase.pitch:
		#find the lowest_pitch of the piece
		if getPosPitchList(each_pitch)<getPosPitchList(lowest_pitch):
			lowest_pitch = each_pitch
		
			#find the highest_pitch of the piece
		if getPosPitchList(each_pitch)>getPosPitchList(highest_pitch):
			highest_pitch = each_pitch
		
	return base_pitch, final_pitch, lowest_pitch, highest_pitch











#==============================================================================
class TestTracker(unittest.TestCase):
	def test_modality(self):
		self.assertEqual('', '')


if __name__ == '__main__':
	unittest.main()



